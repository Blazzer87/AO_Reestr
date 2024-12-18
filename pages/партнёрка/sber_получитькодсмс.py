https://id-psi.sber.ru/CSAFront/oidc/authorize?client_id=99FC826E-160B-A9C4-FC72-EB5D703FD64B&redirect_uri=https%3A%2F%2Flocalhost%3A441%2Fapi%2Fv1%2Fsberid%2Fauthentication_callback&scope=openid%20maindoc%20birthdate%20email%20mobile%20name%20inn&response_type=code&state=3e284950-9aa5-4b56-b2d2-3e67998c0bfb&nonce=569a1359-e0c5-4c18-b14b-489849b24d65

кнопка получить код смс
$x('//button[@data-testid="confirmOptions-sms"]')

кнопки ввода смс - 5 штук
$x('//input[@name="sms0"]')
$x('//input[@name="sms1"]')
$x('//input[@name="sms2"]')
$x('//input[@name="sms3"]')
$x('//input[@name="sms4"]')

блок в котором всё находится для проверки на видимость
$x('//form[@data-testid="smsCodeInputForm"]')

поле ввода кода из письма
$x('//input[@data-testid="emailCodeInput"]')


ЕСЛИ ЕСТЬ КНОПКА
$x('//button[@data-testid="ITS_NOT_MI"]')
то нажми кнопку продолжить
$x('//button[@data-testid="APPROVE_BUTTON"]')


потом сразу на страницу услуг
