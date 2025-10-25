# Отчет по лабораторной работе №5
## "Знакомство с CI/CD"

### 1. Workflow файл

```yaml
name: Run Unit Tests

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
    
    runs-on: ${{ matrix.os }}
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
      
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: Display Python version
      run: python -c "import sys; print('Python version:', sys.version)"
      
    - name: Run unit tests
      run: python -m unittest test_geometry.py
      
    - name: Test completion message
      run: echo "Unit tests completed successfully"
```
### Workflow запускается при каждом push в репозиторий, а также при создании pull request

### 3. Структура проекта
```text
geometric_lib/
├── .github/
│   └── workflows/
│       └── main.yml          # Workflow файл CI/CD
├── circle.py   
├── rectangle.py
├── sqare.py
├── triangle.py
├── test_geometry.py          # Unit-тесты из лаб. работы №4
├── geometry.py
└── README.md
```
### Результаты работы
![CI/CD Workflow Results](https://github.com/Arseniy281/geometric_lib/raw/main/github_workflow_lab_isrpo_5.png)

### Текстовое представление результатов:
```text
Run Unit Tests #1
✓ Completed in 1m 23s

Jobs:
✓ test (ubuntu-latest) • 45s
✓ test (windows-latest) • 38s

Matrix:
✓ ubuntu-latest
✓ windows-latest

Все шаги выполнены успешно:
✓ actions/checkout@v4
✓ actions/setup-python@v4
✓ python -c "import sys; print('Python:', sys.version)"
✓ python -m unittest test_geometry.py
Детали выполнения:
На Ubuntu Linux:

Python version: 3.9.18

21 tests passed

Время выполнения: ~45 секунд

На Windows Server:

Python version: 3.9.18

21 tests passed

Время выполнения: ~38 секунд
```