import subprocess
import sys
import os

REPO_PATH = os.path.expanduser('~/Sites/python_rtk')
BRANCH = 'main'


def run_command(cmd, cwd=None, input_text=None):
    print(f"> {' '.join(cmd)}")
    result = subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        input=input_text,
        capture_output=True
    )
    if result.returncode != 0:
        print(f"Ошибка при выполнении команды: {' '.join(cmd)}")
        print(result.stderr)
        sys.exit(result.returncode)
    return result.stdout.strip()


def main():
    if not os.path.exists(REPO_PATH):
        print(f"Папка репозитория не найдена: {REPO_PATH}")
        sys.exit(1)

    # Запуск фильтрации истории для удаления токенов ghp_
    replace_text = "ghp_==REMOVED"
    print("Запуск git-filter-repo для удаления токенов ghp_ из истории...")
    run_command(['git', 'filter-repo', '--replace-text', '-'],
                cwd=REPO_PATH, input_text=replace_text)

    # Проверяем, остались ли токены
    print("Проверка наличия токенов ghp_ в истории...")
    log_output = run_command(
        ['git', 'log', '-p', '--', 'part 2/Lesson 11/11.ipynb'], cwd=REPO_PATH)
    if "ghp_" in log_output:
        print("Токены ghp_ все еще найдены! Проверьте очистку вручную.")
        sys.exit(2)

    # Принудительный пуш
    print(f"Выполняем принудительный пуш в ветку {BRANCH}...")
    run_command(['git', 'push', '--force', '--set-upstream',
                'origin', BRANCH], cwd=REPO_PATH)

    print("Готово! После этого не забудьте предупредить коллег выполнить:")
    print("  git fetch")
    print(f"  git reset --hard origin/{BRANCH}")


if __name__ == '__main__':
    main()
