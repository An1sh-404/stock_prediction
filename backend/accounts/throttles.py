from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class LoginThrottle(AnonRateThrottle):
    scope = 'login'

class ResendThrottle(AnonRateThrottle):
    scope='resend_verification'

class VerifyThrottle(AnonRateThrottle):
    scope='verify_email'

class RegistrationThrottle(AnonRateThrottle):
    scope='registration'



class BurstRateThrottle(UserRateThrottle):
    scope = "burst"


class SustainedRateThrottle(UserRateThrottle):
    scope = "sustained"