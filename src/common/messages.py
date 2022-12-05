from enum import Enum


class Messages(Enum):
    translate = {
        "This field is required.": "این فیلد الزامی است",
        "UNIQUE_CATEGORY": 'این دسته بندی برای این رستوران وجود دارد',
        "UNIQUE_FOOD": 'این غذا در این دسنه بندی وجود دارد',
        "UNIQUE_ORDER": 'این غذا در حال حاضر در سبد شما موجود می باشد',
        "Invalid value.": "مقدار نامعتبر",
        "permission_denied": "شما اجازه انجام این عمل را ندارید",
        "Not found.": "پیدا نشد",
        "token_not_valid": "توکن نامعتبر است یا منقضی شده است",
        "throttled": "درخواست مسدود شد انتظار می رود در {} ثانیه در دسترس باشد",
        "method_not_allowed":"{} مجاز نیست",
        "valid ObjectId": '{}  معتبر نیست',
        "NOT_AUTHENTICATED": 'شما از سایت خارج شدید برای ورود مجدد لاگین کنید',
        'Token is blacklisted': 'توکن منقضی شده است',
        'Token is invalid or expired': 'توکن نامعتبر است یا منقضی شده است'
    }