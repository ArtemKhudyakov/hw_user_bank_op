# import src.masks

# import src.generators as gen
# import src.utils as utils
import src.processing

# import src.widjet

#
# card_number: str = str(7000792289606361)
# acc_number: str = str(73654108430135874305)
# masked_card_number: str = src.masks.get_mask_card_number(card_number)
# masked_acc_number: str = src.masks.get_mask_account(acc_number)
# print(masked_card_number)
# print(masked_acc_number)
# print()
#
# data = [
#     "Maestro 1596837868705199",
#     "Счет 64686473678894779589",
#     "MasterCard 7158300734726758",
#     "Счет 35383033474447895560",
#     "Visa Classic 6831982476737658",
#     "Visa Platinum 8990922113665229",
#     "Visa Gold 5999414228426353",
#     "Счет 73654108430135874305",
#     "Visa Gold 5999414228426",
#     "fdsf",
#     "",
# ]
#
# dates = [
#     "2024-03-11T02:26:18.671407",
#     "2025-12-11T02:26:18.671407",
#     "",
#     "Error",
# ]
#
# operations_data = [
#     {
#         "id": "41428829",
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#     },
#     {
#         "id": "939719570",
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#     },
#     {
#         "id": "594226727",
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#     },
#     {
#         "id": "615064591",
#         "state": "CANCELED",
#         "date": "2018-10-14T08:21:33.419441",
#     },
# ]
#

operations_list = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 214024827,
        "state": "EXECUTED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {
            "amount": "70946.18",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366",
    },
    {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-07-12T20:41:47.882230",
        "operationAmount": {
            "amount": "51463.70",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 48894435694657014368",
        "to": "Счет 38976430693692818358",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {
            "amount": "79931.03",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215",
    },
    {
        "id": 716496732,
        "state": "EXECUTED",
        "date": "2018-04-04T17:33:34.701093",
        "operationAmount": {
            "amount": "40701.91",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Visa Gold 5999414228426353",
        "to": "Счет 72731966109147704472",
    },
    {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {
            "amount": "41096.24",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
    {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
        "operationAmount": {
            "amount": "77751.04",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 3928549031574026",
        "to": "Счет 84163357546688983493",
    },
    {
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2018-01-26T15:40:13.413061",
        "operationAmount": {
            "amount": "50870.71",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 4598300720424501",
        "to": "Счет 43597928997568165086",
    },
    {
        "id": 518707726,
        "state": "EXECUTED",
        "date": "2018-11-29T07:18:23.941293",
        "operationAmount": {
            "amount": "3348.98",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "MasterCard 3152479541115065",
        "to": "Visa Gold 9447344650495960",
    },
    {
        "id": 649467725,
        "state": "EXECUTED",
        "date": "2018-04-14T19:35:28.978265",
        "operationAmount": {
            "amount": "96995.73",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Счет 27248529432547658655",
        "to": "Счет 97584898735659638967",
    },
    {
        "id": 782295999,
        "state": "EXECUTED",
        "date": "2019-09-11T17:30:34.445824",
        "operationAmount": {
            "amount": "54280.01",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 24763316288121894080",
        "to": "Счет 96291777776753236930",
    },
    {
        "id": 542678139,
        "state": "EXECUTED",
        "date": "2018-10-14T22:27:25.205631",
        "operationAmount": {
            "amount": "90582.51",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 2256483756542539",
        "to": "Счет 78808375133947439319",
    },
    {
        "id": 558167602,
        "state": "EXECUTED",
        "date": "2019-04-12T17:27:27.896421",
        "operationAmount": {
            "amount": "43861.89",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 73654108430135874305",
        "to": "Счет 89685546118890842412",
    },
    {
        "id": 407169720,
        "state": "EXECUTED",
        "date": "2018-02-03T14:52:08.093722",
        "operationAmount": {
            "amount": "67011.26",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на карту",
        "from": "MasterCard 4047671689373225",
        "to": "Maestro 3806652527413662",
    },
    {
        "id": 361044570,
        "state": "EXECUTED",
        "date": "2018-03-02T02:03:11.563721",
        "operationAmount": {
            "amount": "7484.91",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 96008924215040031147",
        "to": "Счет 30377212495530283001",
    },
    {
        "id": 536723678,
        "state": "EXECUTED",
        "date": "2018-06-12T07:17:01.311610",
        "operationAmount": {
            "amount": "26334.08",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Visa Classic 4195191172583802",
        "to": "Счет 17066032701791012883",
    },
    {
        "id": 172864002,
        "state": "EXECUTED",
        "date": "2018-12-28T23:10:35.459698",
        "operationAmount": {
            "amount": "49192.52",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Открытие вклада",
        "to": "Счет 96231448929365202391",
    },
    {
        "id": 476991061,
        "state": "CANCELED",
        "date": "2018-11-23T17:47:33.127140",
        "operationAmount": {
            "amount": "26971.25",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Gold 7305799447374042",
        "to": "Maestro 3364923093037194",
    },
    {
        "id": 633268359,
        "state": "EXECUTED",
        "date": "2019-07-12T08:11:47.735774",
        "operationAmount": {
            "amount": "2631.44",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Gold 3589276410671603",
        "to": "Счет 96292138399386853355",
    },
    {
        "id": 988276204,
        "state": "EXECUTED",
        "date": "2018-02-22T00:40:19.984219",
        "operationAmount": {
            "amount": "71771.90",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 4956649687637418",
        "to": "Счет 90562872508279542248",
    },
    {
        "id": 888407131,
        "state": "EXECUTED",
        "date": "2019-09-29T14:25:28.588059",
        "operationAmount": {
            "amount": "45849.53",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 35421428450077339637",
        "to": "Счет 46723050671868944961",
    },
    {
        "id": 634356296,
        "state": "EXECUTED",
        "date": "2018-01-21T01:10:28.317704",
        "operationAmount": {
            "amount": "96900.90",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 33407225454123927865",
        "to": "Счет 79619011266276091215",
    },
    {
        "id": 34148726,
        "state": "EXECUTED",
        "date": "2018-11-23T23:52:36.999661",
        "operationAmount": {
            "amount": "79428.73",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Platinum 5355133159258236",
        "to": "Maestro 8045769817179061",
    },
    {
        "id": 970724427,
        "state": "CANCELED",
        "date": "2019-01-15T17:58:27.064377",
        "operationAmount": {
            "amount": "90688.44",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 2241653116508487",
        "to": "Счет 26494285169417058486",
    },
    {
        "id": 104807525,
        "state": "EXECUTED",
        "date": "2019-06-01T06:46:16.803326",
        "operationAmount": {
            "amount": "60888.63",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на счет",
        "from": "МИР 8201420097886664",
        "to": "Счет 35116633516390079956",
    },
    {
        "id": 550607912,
        "state": "EXECUTED",
        "date": "2018-07-31T12:25:32.579413",
        "operationAmount": {
            "amount": "34380.08",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 8532498887072395",
        "to": "Счет 44238164562083919420",
    },
    {
        "id": 608117766,
        "state": "CANCELED",
        "date": "2018-10-08T09:05:05.282282",
        "operationAmount": {
            "amount": "77302.31",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Gold 6527183396477720",
        "to": "Счет 38573816654581789611",
    },
    {
        "id": 484201274,
        "state": "EXECUTED",
        "date": "2019-04-11T23:10:21.514616",
        "operationAmount": {
            "amount": "62621.51",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на карту",
        "from": "МИР 8193813157568899",
        "to": "МИР 9425591958944146",
    },
    {
        "id": 547682597,
        "state": "EXECUTED",
        "date": "2018-12-29T21:45:18.495053",
        "operationAmount": {
            "amount": "66263.93",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Счет 77977573135347241529",
        "to": "Счет 33062909508148771891",
    },
    {
        "id": 811920303,
        "state": "EXECUTED",
        "date": "2019-06-14T19:37:49.044089",
        "operationAmount": {
            "amount": "63150.74",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 73222753239048295679",
        "to": "Счет 78544755774551298747",
    },
    {
        "id": 509645757,
        "state": "EXECUTED",
        "date": "2019-10-30T01:49:52.939296",
        "operationAmount": {
            "amount": "23036.03",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Gold 7756673469642839",
        "to": "Счет 48943806953649539453",
    },
    {
        "id": 801684332,
        "state": "EXECUTED",
        "date": "2019-11-05T12:04:13.781725",
        "operationAmount": {
            "amount": "21344.35",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Открытие вклада",
        "to": "Счет 77613226829885488381",
    },
    {
        "id": 122284694,
        "state": "EXECUTED",
        "date": "2019-08-08T21:58:06.688541",
        "operationAmount": {
            "amount": "98657.83",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Счет 99668626339273709694",
        "to": "Счет 27219929444683698245",
    },
    {
        "id": 154927927,
        "state": "EXECUTED",
        "date": "2019-11-19T09:22:25.899614",
        "operationAmount": {
            "amount": "30153.72",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Maestro 7810846596785568",
        "to": "Счет 43241152692663622869",
    },
    {
        "id": 743628025,
        "state": "EXECUTED",
        "date": "2018-06-04T06:59:55.424356",
        "operationAmount": {
            "amount": "978.31",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 54883981902864782073",
        "to": "Счет 61834060137088759145",
    },
    {
        "id": 743278119,
        "state": "EXECUTED",
        "date": "2018-10-15T08:05:34.061711",
        "operationAmount": {
            "amount": "51203.12",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "MasterCard 1435442169918409",
        "to": "Maestro 7452400219469235",
    },
    {
        "id": 871921546,
        "state": "EXECUTED",
        "date": "2019-02-14T03:09:23.006652",
        "operationAmount": {
            "amount": "47022.09",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Classic 6216537926639975",
        "to": "Счет 67667879435628279708",
    },
    {
        "id": 373912477,
        "state": "EXECUTED",
        "date": "2018-03-09T02:11:01.339352",
        "operationAmount": {
            "amount": "33249.01",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Classic 7022985698476865",
        "to": "Счет 60979028617970883410",
    },
    {
        "id": 720751477,
        "state": "EXECUTED",
        "date": "2018-11-08T08:21:45.902633",
        "operationAmount": {
            "amount": "16872.46",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75743795418434298755",
        "to": "Счет 80785963509390811744",
    },
    {
        "id": 949194534,
        "state": "EXECUTED",
        "date": "2019-08-15T01:48:10.042554",
        "operationAmount": {
            "amount": "31222.43",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Счет 65298957349197687907",
        "to": "Счет 38784565940893479418",
    },
    {
        "id": 260972664,
        "state": "EXECUTED",
        "date": "2018-01-23T01:48:30.477053",
        "operationAmount": {
            "amount": "2974.30",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 3414396880443483",
        "to": "Visa Gold 2684274847577419",
    },
    {
        "id": 317987878,
        "state": "EXECUTED",
        "date": "2018-01-13T13:00:58.458625",
        "operationAmount": {
            "amount": "55985.82",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 8906171742833215",
        "to": "Visa Platinum 6086997013848217",
    },
    {
        "id": 72122709,
        "state": "EXECUTED",
        "date": "2018-12-18T17:07:09.800800",
        "operationAmount": {
            "amount": "19683.25",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 86675623828180311969",
        "to": "Счет 15351391408911677994",
    },
    {
        "id": 242885401,
        "state": "EXECUTED",
        "date": "2019-07-08T00:08:32.986663",
        "operationAmount": {
            "amount": "10083.68",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 38427597486442637521",
        "to": "Счет 83889757415570699323",
    },
    {
        "id": 286706711,
        "state": "EXECUTED",
        "date": "2018-02-06T06:42:02.219233",
        "operationAmount": {
            "amount": "621.37",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "MasterCard 9175985085449563",
        "to": "Счет 82781399328834147668",
    },
    {
        "id": 108066781,
        "state": "EXECUTED",
        "date": "2019-06-21T12:34:06.351022",
        "operationAmount": {
            "amount": "25762.92",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Открытие вклада",
        "to": "Счет 90817634362091276762",
    },
    {
        "id": 100392079,
        "state": "EXECUTED",
        "date": "2019-03-03T03:13:18.622393",
        "operationAmount": {
            "amount": "44493.45",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Classic 6319351940209800",
        "to": "Счет 14073196441261107791",
    },
    {
        "id": 51314762,
        "state": "EXECUTED",
        "date": "2018-08-25T02:58:18.764678",
        "operationAmount": {
            "amount": "52245.30",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 4040551273087672",
        "to": "Visa Platinum 7825450883088021",
    },
    {
        "id": 464419177,
        "state": "CANCELED",
        "date": "2018-07-15T18:44:13.346362",
        "operationAmount": {
            "amount": "71024.64",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Gold 9657499677062945",
        "to": "Счет 19213886662094884261",
    },
    {
        "id": 560813069,
        "state": "CANCELED",
        "date": "2019-12-03T04:27:03.427014",
        "operationAmount": {
            "amount": "17628.50",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "MasterCard 1796816785869527",
        "to": "Visa Classic 7699855375169288",
    },
    {
        "id": 894961746,
        "state": "EXECUTED",
        "date": "2019-08-04T20:17:25.443322",
        "operationAmount": {
            "amount": "2523.44",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 33721541831646393763",
        "to": "Счет 68774571780974952778",
    },
    {
        "id": 360577236,
        "state": "EXECUTED",
        "date": "2019-09-07T07:20:13.889610",
        "operationAmount": {
            "amount": "18536.73",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на карту",
        "from": "Maestro 4284341727554246",
        "to": "МИР 1582474475547301",
    },
    {
        "id": 285353808,
        "state": "EXECUTED",
        "date": "2018-08-06T16:22:54.643491",
        "operationAmount": {
            "amount": "82946.19",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Открытие вклада",
        "to": "Счет 12189246980267075758",
    },
    {
        "id": 416017997,
        "state": "EXECUTED",
        "date": "2019-05-07T01:32:37.142797",
        "operationAmount": {
            "amount": "29033.65",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "МИР 4878656375033856",
        "to": "Maestro 6890749237669619",
    },
    {
        "id": 556488059,
        "state": "CANCELED",
        "date": "2019-05-17T01:50:00.166954",
        "operationAmount": {
            "amount": "74604.56",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "МИР 8021883699486544",
        "to": "Visa Gold 8702717057933248",
    },
    {
        "id": 74897425,
        "state": "EXECUTED",
        "date": "2019-02-08T09:09:35.038506",
        "operationAmount": {
            "amount": "62654.30",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 28429442875257789335",
        "to": "Счет 95473010446151855633",
    },
    {
        "id": 636137913,
        "state": "EXECUTED",
        "date": "2019-06-16T22:17:01.825020",
        "operationAmount": {
            "amount": "24260.78",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Platinum 8990850370884895",
        "to": "Счет 15574304810835774010",
    },
    {
        "id": 813238385,
        "state": "EXECUTED",
        "date": "2018-05-04T03:29:30.253483",
        "operationAmount": {
            "amount": "22007.02",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на счет",
        "from": "MasterCard 3595832182277400",
        "to": "Счет 79697233246085035210",
    },
    {
        "id": 854048120,
        "state": "EXECUTED",
        "date": "2019-03-29T10:57:20.635567",
        "operationAmount": {
            "amount": "30234.99",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на счет",
        "from": "Visa Classic 1203921041964079",
        "to": "Счет 34616199494072692721",
    },
    {
        "id": 269462132,
        "state": "EXECUTED",
        "date": "2018-08-14T05:42:30.104666",
        "operationAmount": {
            "amount": "19010.50",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 18125798580985711166",
        "to": "Счет 98841213648056852372",
    },
    {
        "id": 692008409,
        "state": "CANCELED",
        "date": "2019-02-14T17:38:09.910336",
        "operationAmount": {
            "amount": "37044.95",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Classic 4610247282706784",
        "to": "Счет 63229171188548882700",
    },
    {
        "id": 431131847,
        "state": "EXECUTED",
        "date": "2018-05-05T01:38:56.538074",
        "operationAmount": {
            "amount": "56071.02",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод с карты на счет",
        "from": "MasterCard 9454780748494532",
        "to": "Счет 51958934737718181351",
    },
    {
        "id": 15948212,
        "state": "EXECUTED",
        "date": "2018-12-23T11:47:52.403285",
        "operationAmount": {
            "amount": "47408.20",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "МИР 8665240839126074",
        "to": "Maestro 3000704277834087",
    },
    {
        "id": 114832369,
        "state": "EXECUTED",
        "date": "2019-12-07T06:17:14.634890",
        "operationAmount": {
            "amount": "48150.39",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Visa Classic 2842878893689012",
        "to": "Счет 35158586384610753655",
    },
    {
        "id": 176798279,
        "state": "CANCELED",
        "date": "2019-04-18T11:22:18.800453",
        "operationAmount": {
            "amount": "73778.48",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Открытие вклада",
        "to": "Счет 90417871337969064865",
    },
    {
        "id": 482520625,
        "state": "EXECUTED",
        "date": "2019-11-13T17:38:04.800051",
        "operationAmount": {
            "amount": "62814.53",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 38611439522855669794",
        "to": "Счет 46765464282437878125",
    },
    {
        "id": 414894334,
        "state": "EXECUTED",
        "date": "2019-06-30T15:11:53.136004",
        "operationAmount": {
            "amount": "95860.47",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 59956820797131895975",
        "to": "Счет 43475624104328495820",
    },
    {},
]


transactions = [
    {
        "id": "939719570",
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": "142264268",
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": "873106923",
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": "895315941",
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": "594226727",
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]
#
#
# for number in data:
#     try:
#         print(src.widjet.mask_account_card(number))
#     except ValueError:
#         print("Input error")
#
# print()
# for date in dates:
#     try:
#         print(src.widjet.get_date(date))
#     except ValueError:
#         print("Input error")
#
# print()
#
try:
    for operation in src.processing.filter_by_state(operations_list):
        try:
            print(operation)
        except ValueError:
            print("Input error")
except ValueError:
    print("Input error")
#
# print()
#
# sorted_operations = src.processing.sort_by_date(operations_data)
# for operation in sorted_operations:
#     print(operation)
# print()
# for operation in src.processing.sort_by_date(
#     src.processing.filter_by_state(operations_data), False
# ):
#     print(operation)
#
#
#
#
# currency = input("Введите валюту для фильтрации (RUB, USD, EUR)").upper()
#
# print("Проверка filter_by_currency")
# try:
#     usd_transactions = gen.filter_by_currency(transactions, currency)
#     if not list(usd_transactions):
#         print("Транзакции в данной валюте не производились")
#     else:
#         usd_transactions = gen.filter_by_currency(transactions, currency)
#         print(list(usd_transactions))
# except ValueError:
#     print("Список транзакций пуст")
#
# print("####")
# print("Проверка filter_by_currency, если список пустой")
#
# try:
#     usd_transactions = gen.filter_by_currency([])
#     if not list(usd_transactions):
#         print("Транзакции в данной валюте не производились")
#     else:
#         usd_transactions = gen.filter_by_currency([])
#         print(list(usd_transactions))
# except ValueError:
#     print("Список транзакций пуст")
#
# print("#####")
# print("Проверка transaction_descriptions")
#
# try:
#     description = gen.transaction_descriptions(transactions)
#     print(next(description))
#     print(next(description))
#
#     description = gen.transaction_descriptions([])
#     print(next(description))
# except ValueError:
#     print("Список транзакций пуст")
#
# print("####")
# print(
#     "Проверка transaction_descriptions после фильтрации"
#     " функцией filter_by_currency"
# )
#
# try:
#     filtered = list(gen.filter_by_currency(transactions, currency))
#     filtered_descriptions = gen.transaction_descriptions(filtered)
#     for _ in range(len(filtered)):
#         print(next(filtered_descriptions))
# except StopIteration:
#     print("Транзакции закончились")
#
# except ValueError:
#     print("Список транзакций пуст")

# print("####")
# print("Проверка card_number_generator")


# card_numbers = gen.card_number_generator(1, 10000000)
# try:
#     for i in range(1000000):
#         print(next(card_numbers))
# except StopIteration:
#     print("Хватит уже")

# from typing import Any

# import src.external_api as ext

# transaction_ex: dict[str, Any] = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#         "amount": "8221.37",
#         "currency": {"name": "USD", "code": "USD"},
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560",
# }
#
# try:
#     print(
#         f"{transaction_ex["operationAmount"]["amount"]} "
#         f"{transaction_ex["operationAmount"]["currency"]["code"]}\n"
#         f"{ext.convert_into_rub(transaction_ex)} руб"
#     )
# except Exception as e:
#     print(f"Ошибка: {e} {type(e).__name__}")


# tansac = utils.transactions_data('data/operations.json')
#
# if tansac:
#     for transaction in tansac:
#
#         print(transaction)
#         print()

# import src.data_reader as dr
#
# data = dr.csv_reader("data/transactions.csv")
# for row in data:
#     print(row)

# data = dr.xlsx_reader("data/transaction_excel.xlsx")
# for i in range(0, 2):
#     print(f"{i}--->{data[i]}")
#
#
# for i, row in enumerate(data):
#     if i <= 2:
#         print(i, row)
