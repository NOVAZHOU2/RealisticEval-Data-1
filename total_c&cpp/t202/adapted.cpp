#include <stdexcept>

int getDaysInMonth(int year, int month)
{
    // 检查月份是否有效
    if (month < 1 || month > 12)
    {
        throw std::invalid_argument("Month must be between 1 and 12.");
    }

    // 每个月的天数数组，索引 0 被保留，1-12 代表 1月到12月
    static const int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // 处理二月份的情况
    if (month == 2)
    {
        // 判断是否为闰年
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
        {
            return 29; // 闰年
        }
        else
        {
            return 28; // 非闰年
        }
    }

    // 返回对应月份的天数
    return daysInMonth[month];
}
