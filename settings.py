from os import environ


SESSION_CONFIGS = [
    dict(
        name='min_wage_removal',
        app_sequence=['encoding_simple', 'min_wage_removal', 'survey_mwre'],
        num_demo_participants=2,
    ),
    dict(
        name='min_wage_implementation',
        app_sequence=['encoding_simple', 'min_wage_implementation', 'survey_mwre'],
        num_demo_participants=2,
    ),
]

PARTICIPANT_FIELDS = ['match', 'encoding_payoff']


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=2.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', 
        display_name='Room for live demo (no participant labels)'
    ),
    dict(
        name='min_wage_removal', 
        display_name='Room for min wage removal treatment',
        participant_label_file='_rooms/participant_label.txt',
    ),
    dict(
        name='min_wage_addition', 
        display_name='Room for min wage implementation treatment',
        participant_label_file='_rooms/participant_label.txt',
    ),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '3922710227462'

INSTALLED_APPS = ['otree']
