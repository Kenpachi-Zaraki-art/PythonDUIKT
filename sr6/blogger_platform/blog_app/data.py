class BloggerData:

    def __init__(self):
        self.bloggers = {
            'mrbeast': {
                'name': 'MrBeast (Містер Біст)',
                'category': 'Розваги/Філантропія',
                'description': 'Відомий своїми масштабними трюками та благодійністю.',
                'last_video': 'Я Роздав 100 Автомобілів',
                'social_links': {
                    'youtube': 'https://www.youtube.com/user/MrBeast6000',
                    'twitter': 'https://twitter.com/MrBeast'
                }
            },
            'linustech': {
                'name': 'Linus Tech Tips',
                'category': 'Технології',
                'description': 'Огляди техніки, збірки ПК та технологічні розваги.',
                'last_video': 'Ми Зібрали ПК за $50,000',
                'social_links': {
                    'youtube': 'https://www.youtube.com/user/LinusTechTips',
                    'twitter': 'https://twitter.com/LinusTech'
                }
            },
            'gordonramsay': {
                'name': 'Gordon Ramsay (Ґордон Рамзі)',
                'category': 'Кулінарія',
                'description': 'Всесвітньо відомий шеф-кухар та телеведучий.',
                'last_video': 'Туторіал з Приготування Ідеального Стейка',
                'social_links': {
                    'youtube': 'https://www.youtube.com/c/gordonramsay',
                    'instagram': 'https://www.instagram.com/gordongram'
                }
            },
            'komarov': {
                'name': 'Дмитро Комаров',
                'category': 'Подорожі/Документалістика',
                'description': 'Автор та ведучий програми "Світ Навиворіт".',
                'last_video': 'Рік. За Кадром. Спецпроект',
                'social_links': {
                    'youtube': 'https://www.youtube.com/channel/UCF-20CgLClB_H_S-M7nnkVA',
                    'instagram': 'https://www.instagram.com/svit.navyvorit/'
                }
            },
            'jerryheil': {
                'name': 'Jerry Heil',
                'category': 'Музика/Влоги',
                'description': 'Українська співачка, авторка пісень та відеоблогерка.',
                'last_video': 'Teresa & Maria - Eurovision 2024',
                'social_links': {
                    'youtube': 'https://www.youtube.com/c/JerryHeil',
                    'instagram': 'https://www.instagram.com/thejerryheil/'
                }
            }
        }

        self.news = [
            {'date': '2025-11-17', 'title': 'MrBeast відкриває новий благодійний проект!'},
            {'date': '2025-11-16', 'title': 'Linus Tech Tips робить огляд на нову GPU.'},
            {'date': '2025-11-15', 'title': 'Ґордон Рамзі запускає новий ресторан.'},
            {'date': '2025-11-14', 'title': 'Дмитро Комаров анонсував новий сезон.'},
            {'date': '2025-11-13', 'title': 'Jerry Heil випустила новий хіт.'},
        ]

    def get_all_bloggers(self):
        return self.bloggers

    def get_blogger_by_slug(self, slug):
        return self.bloggers.get(slug)

    def get_news(self):
        return self.news