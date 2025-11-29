"""
Скрипт для заповнення бази даних тестовими даними
Запуск: python populate_db_script.py
"""

import os
import django
import random
from datetime import datetime, timedelta

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NextStep_School.settings')
django.setup()

# Імпорт моделей після налаштування Django
from django.contrib.auth.models import User
from home_app.models import Announcement
from course_and_module_app.models import Course, Module, ModuleSchedule
from lessons_app.models import Lesson, LessonSchedule, Material
from tasksmarks_app.models import Task, TestTask, Option, ChoiceTest, AnswerTask


def clear_database():
    """Очищення існуючих даних"""
    print('Clearing existing data...')
    ChoiceTest.objects.all().delete()
    AnswerTask.objects.all().delete()
    Option.objects.all().delete()
    TestTask.objects.all().delete()
    Task.objects.all().delete()
    LessonSchedule.objects.all().delete()
    Lesson.objects.all().delete()
    Material.objects.all().delete()
    ModuleSchedule.objects.all().delete()
    Module.objects.all().delete()
    Course.objects.all().delete()
    Announcement.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()
    print('✓ Data cleared')


def create_users():
    """Створення користувачів"""
    print('\nCreating users...')

    # Створення адміністратора
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            first_name='Admin',
            last_name='User'
        )
        print(f'✓ Created admin: {admin.username}')
    else:
        admin = User.objects.get(username='admin')
        print(f'✓ Admin already exists: {admin.username}')

    # Створення вчителів
    teachers = []
    teacher_data = [
        ('teacher1', 'Іван', 'Петренко', 'teacher1@example.com'),
        ('teacher2', 'Марія', 'Коваленко', 'teacher2@example.com'),
        ('teacher3', 'Олександр', 'Шевченко', 'teacher3@example.com'),
    ]

    for username, first_name, last_name, email in teacher_data:
        teacher = User.objects.create_user(
            username=username,
            email=email,
            password='teacher123',
            first_name=first_name,
            last_name=last_name
        )
        teachers.append(teacher)
        print(f'✓ Created teacher: {teacher.username}')

    # Створення студентів
    students = []
    student_data = [
        ('student1', 'Андрій', 'Мельник', 'student1@example.com'),
        ('student2', 'Ольга', 'Бондаренко', 'student2@example.com'),
        ('student3', 'Дмитро', 'Кравченко', 'student3@example.com'),
        ('student4', 'Анна', 'Лисенко', 'student4@example.com'),
        ('student5', 'Сергій', 'Павленко', 'student5@example.com'),
        ('student6', 'Тетяна', 'Гриценко', 'student6@example.com'),
        ('student7', 'Максим', 'Ткаченко', 'student7@example.com'),
        ('student8', 'Катерина', 'Романенко', 'student8@example.com'),
    ]

    for username, first_name, last_name, email in student_data:
        student = User.objects.create_user(
            username=username,
            email=email,
            password='student123',
            first_name=first_name,
            last_name=last_name
        )
        students.append(student)
        print(f'✓ Created student: {student.username}')

    return admin, teachers, students


def create_announcements(teachers, admin):
    """Створення оголошень"""
    print('\nCreating announcements...')
    announcements_data = [
        ('Ласкаво просимо до NextStep School!',
         'Ми раді вітати вас у нашій навчальній системі. Тут ви знайдете всі необхідні матеріали для навчання.'),
        ('Початок нового семестру',
         'Новий семестр починається 1 грудня. Просимо всіх студентів зареєструватися на курси.'),
        ('Оновлення розкладу',
         'Розклад занять було оновлено. Перевірте розділ з розкладом для детальної інформації.'),
        ('Важливо: Терміни здачі завдань',
         'Нагадуємо про важливість своєчасної здачі домашніх завдань. Дотримуйтесь дедлайнів!'),
        ('Технічне обслуговування',
         'Планується технічне обслуговування системи 25 листопада з 22:00 до 24:00.'),
    ]

    for title, content in announcements_data:
        announcement = Announcement.objects.create(
            title=title,
            content=content,
            author=random.choice(teachers + [admin])
        )
        print(f'✓ Created announcement: {announcement.title}')


def create_courses(teachers, students):
    """Створення курсів"""
    print('\nCreating courses...')
    courses_data = [
        ('Python для початківців',
         'Основи програмування на Python. Вивчення синтаксису, структур даних та основних концепцій.'),
        ('Web-розробка з Django',
         'Створення веб-додатків за допомогою фреймворку Django. Backend розробка.'),
        ('JavaScript і Frontend',
         'Сучасна frontend розробка з використанням JavaScript, HTML5 та CSS3.'),
        ('Бази даних та SQL',
         'Проектування баз даних, мова SQL, робота з реляційними СУБД.'),
        ('Data Science з Python',
         'Аналіз даних, машинне навчання та візуалізація даних за допомогою Python.'),
    ]

    courses = []
    for i, (name, description) in enumerate(courses_data):
        teacher = teachers[i % len(teachers)]
        course = Course.objects.create(
            name=name,
            description=description,
            teacher=teacher
        )
        # Додавання студентів до курсу
        course_students = random.sample(students, random.randint(4, 7))
        course.students.set(course_students)
        courses.append(course)
        print(f'✓ Created course: {course.name} (Teacher: {teacher.username}, Students: {len(course_students)})')

    return courses


def create_modules(courses):
    """Створення модулів"""
    print('\nCreating modules...')
    modules_data = {
        'Python для початківців': [
            'Введення в Python',
            'Змінні та типи даних',
            'Умовні конструкції та цикли',
            'Функції та модулі',
            'ООП в Python'
        ],
        'Web-розробка з Django': [
            'Введення в Django',
            'Моделі та ORM',
            'Views та Templates',
            'Forms та валідація',
            'Аутентифікація та авторизація'
        ],
        'JavaScript і Frontend': [
            'Основи JavaScript',
            'DOM маніпуляції',
            'Асинхронність та Promise',
            'Сучасний ES6+',
            'React основи'
        ],
        'Бази даних та SQL': [
            'Введення в БД',
            'SQL запити',
            'Нормалізація',
            'Індекси та оптимізація',
            'Транзакції'
        ],
        'Data Science з Python': [
            'NumPy та масиви',
            'Pandas та аналіз даних',
            'Візуалізація з Matplotlib',
            'Scikit-learn основи',
            'Проект: Аналіз даних'
        ]
    }

    modules = []
    start_date = datetime.now()
    for course in courses:
        if course.name in modules_data:
            for i, module_name in enumerate(modules_data[course.name]):
                module = Module.objects.create(
                    name=module_name,
                    course=course
                )
                modules.append(module)

                # Створення розкладу модуля
                module_start = start_date + timedelta(weeks=i * 2)
                ModuleSchedule.objects.create(
                    start_module=module_start,
                    module=module
                )
                print(f'✓ Created module: {module.name}')

    return modules


def create_materials():
    """Створення матеріалів"""
    print('\nCreating materials...')
    materials = []
    material_links = [
        'https://docs.python.org/3/',
        'https://www.djangoproject.com/start/',
        'https://developer.mozilla.org/en-US/docs/Web/JavaScript',
        'https://www.w3schools.com/sql/',
        'https://numpy.org/doc/',
    ]

    for i in range(15):
        material = Material.objects.create(
            link=random.choice(material_links)
        )
        materials.append(material)

    print(f'✓ Created {len(materials)} materials')
    return materials


def create_tasks():
    """Створення звичайних завдань"""
    print('\nCreating tasks...')
    tasks_data = [
        ('Написати функцію для сортування',
         'Створіть функцію, яка приймає список чисел та повертає відсортований список.'),
        ('Калькулятор',
         'Розробіть простий калькулятор з основними операціями: додавання, віднімання, множення, ділення.'),
        ('Робота зі списками',
         'Напишіть програму для видалення дублікатів зі списку.'),
        ('Обробка рядків',
         'Створіть функцію для підрахунку кількості слів у тексті.'),
        ('Словники в Python',
         'Створіть програму для підрахунку частоти слів у тексті використовуючи словник.'),
        ('Django модель',
         'Створіть модель для блогу з полями: заголовок, контент, автор, дата публікації.'),
        ('Django views',
         'Напишіть view для відображення списку статей з пагінацією.'),
        ('SQL запити',
         'Напишіть SQL запит для вибірки всіх користувачів, які зареєструвалися за останній місяць.'),
        ('JavaScript функція',
         'Створіть функцію для валідації email адреси.'),
        ('Аналіз даних',
         'Проаналізуйте наданий CSV файл та знайдіть середнє значення вказаної колонки.'),
    ]

    tasks = []
    for name, description in tasks_data:
        task = Task.objects.create(
            name=name,
            description=description,
            status=random.choice(['todo', 'un_check', 'well', 'wrong'])
        )
        tasks.append(task)
        print(f'✓ Created task: {task.name}')

    return tasks


def create_test_tasks():
    """Створення тестових завдань"""
    print('\nCreating test tasks...')
    test_tasks_data = [
        ('Що таке змінна в Python?', [
            ('Контейнер для зберігання даних', True),
            ('Тип даних', False),
            ('Функція', False),
            ('Клас', False),
        ]),
        ('Який метод HTTP використовується для отримання даних?', [
            ('GET', True),
            ('POST', False),
            ('PUT', False),
            ('DELETE', False),
        ]),
        ('Що таке ORM?', [
            ('Object-Relational Mapping', True),
            ('Object-Resource Manager', False),
            ('Operational Resource Model', False),
            ('Oriented Relational Method', False),
        ]),
        ('Яка команда для міграцій в Django?', [
            ('python manage.py migrate', True),
            ('django migrate', False),
            ('python migrate.py', False),
            ('manage migrate', False),
        ]),
        ('Що повертає функція len() в Python?', [
            ('Кількість елементів', True),
            ('Тип об\'єкта', False),
            ('Значення елемента', False),
            ('Індекс елемента', False),
        ]),
        ('SQL означає...', [
            ('Structured Query Language', True),
            ('Simple Question Language', False),
            ('Standard Query Logic', False),
            ('System Quality Level', False),
        ]),
        ('Який метод для додавання елемента в список Python?', [
            ('append()', True),
            ('add()', False),
            ('insert_last()', False),
            ('push()', False),
        ]),
        ('Що таке DOM?', [
            ('Document Object Model', True),
            ('Data Object Management', False),
            ('Dynamic Online Method', False),
            ('Document Orientation Model', False),
        ]),
    ]

    test_tasks = []
    for question, options_data in test_tasks_data:
        test_task = TestTask.objects.create(
            name=question,
            status=random.choice(['todo', 'well', 'wrong'])
        )
        test_tasks.append(test_task)

        # Створення варіантів відповідей
        for option_text, is_correct in options_data:
            Option.objects.create(
                name=option_text,
                option=test_task,
                is_correct=is_correct
            )

        print(f'✓ Created test task: {test_task.name}')

    return test_tasks


def create_lessons(modules, materials, tasks, test_tasks):
    """Створення уроків"""
    print('\nCreating lessons...')
    lessons = []
    start_date = datetime.now()

    for module in modules:
        for i in range(random.randint(2, 4)):
            lesson_name = f'{module.name} - Урок {i + 1}'
            lesson = Lesson.objects.create(
                name=lesson_name,
                modul=module
            )

            # Додавання матеріалів до уроку
            lesson_materials = random.sample(materials, random.randint(1, 3))
            lesson.material.set(lesson_materials)

            # Додавання завдань до уроку
            if tasks:
                lesson_tasks = random.sample(tasks, min(random.randint(1, 2), len(tasks)))
                lesson.tasks.set(lesson_tasks)

            # Додавання тестових завдань до уроку
            if test_tasks:
                lesson_test_tasks = random.sample(test_tasks, min(random.randint(1, 2), len(test_tasks)))
                lesson.tasks_test.set(lesson_test_tasks)

            lessons.append(lesson)

            # Створення розкладу уроку
            lesson_date = start_date + timedelta(weeks=modules.index(module), days=i * 2)
            LessonSchedule.objects.create(
                start_lessons=lesson_date,
                lesson=lesson
            )

            print(f'✓ Created lesson: {lesson.name}')

    return lessons


def create_student_answers(students, tasks, test_tasks):
    """Створення відповідей студентів"""
    print('\nCreating student answers...')

    # Відповіді на тестові завдання
    for _ in range(30):
        student = random.choice(students)
        test_task = random.choice(test_tasks)
        options = list(test_task.answers.all())
        if options:
            chosen_option = random.choice(options)
            ChoiceTest.objects.create(
                student=student,
                option_choice=chosen_option,
                choice=test_task
            )

    print(f'✓ Created {ChoiceTest.objects.count()} test answers')

    # Відповіді на звичайні завдання
    answers_examples = [
        'Я виконав завдання. Код працює правильно.',
        'Функція створена згідно з вимогами. Додав коментарі.',
        'Завдання виконано. Протестував на різних даних.',
        'Реалізовано всі необхідні методи. Результат у додатку.',
        'Код оптимізовано. Використав рекомендовані практики.',
    ]

    for _ in range(25):
        student = random.choice(students)
        task = random.choice(tasks)
        AnswerTask.objects.create(
            student=student,
            choice=task,
            answer=random.choice(answers_examples)
        )

    print(f'✓ Created {AnswerTask.objects.count()} task answers')


def print_summary(teachers, students):
    """Виведення підсумкової інформації"""
    print('\n' + '=' * 60)
    print('DATABASE POPULATED SUCCESSFULLY!')
    print('=' * 60)
    print(f'\n📊 Statistics:')
    print(f'  Users: {User.objects.count()}')
    print(f'    - Teachers: {len(teachers)}')
    print(f'    - Students: {len(students)}')
    print(f'  Announcements: {Announcement.objects.count()}')
    print(f'  Courses: {Course.objects.count()}')
    print(f'  Modules: {Module.objects.count()}')
    print(f'  Lessons: {Lesson.objects.count()}')
    print(f'  Materials: {Material.objects.count()}')
    print(f'  Tasks: {Task.objects.count()}')
    print(f'  Test Tasks: {TestTask.objects.count()}')
    print(f'  Student Test Answers: {ChoiceTest.objects.count()}')
    print(f'  Student Task Answers: {AnswerTask.objects.count()}')

    print(f'\n🔑 Login credentials:')
    print(f'  Admin: admin / admin123')
    print(f'  Teachers: teacher1, teacher2, teacher3 / teacher123')
    print(f'  Students: student1-8 / student123')
    print('=' * 60 + '\n')


def main():
    """Головна функція"""
    print('=' * 60)
    print('POPULATING DATABASE WITH TEST DATA')
    print('=' * 60)

    try:
        # Очищення БД
        clear_database()

        # Створення даних
        admin, teachers, students = create_users()
        create_announcements(teachers, admin)
        courses = create_courses(teachers, students)
        modules = create_modules(courses)
        materials = create_materials()
        tasks = create_tasks()
        test_tasks = create_test_tasks()
        lessons = create_lessons(modules, materials, tasks, test_tasks)
        create_student_answers(students, tasks, test_tasks)

        # Виведення підсумку
        print_summary(teachers, students)

    except Exception as e:
        print(f'\n❌ Error: {e}')
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    main()
