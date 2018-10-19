"""Auto-generated file, do not edit by hand. ID metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_ID = PhoneMetadata(id='ID', country_code=62, international_prefix='0(?:0[17-9]|10(?:00|1[67]))',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[1-36]|8\\d{5})\\d{6}|[1-9]\\d{8,10}|[2-9]\\d{7}', possible_length=(7, 8, 9, 10, 11, 12), possible_length_local_only=(5, 6)),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:[124]\\d{7,8}|(?:[35][1-4]|6[0-8]|7[1-6]|8\\d|9[1-8])\\d{5,8})|(?:3(?:1|[25][1-8]|3[1-68]|4[1-3]|6[1-3568]|7[0-469]|8\\d)|4(?:0[1-589]|1[01347-9]|2[0-36-8]|3[0-24-68]|43|5[1-378]|6[1-5]|7[134]|8[1245])|5(?:1[1-35-9]|2[25-8]|3[124-9]|4[1-3589]|5[1-46]|6[1-8])|7(?:02|[125][1-9]|[36]\\d|4[1-8]|7[0-36-9])|9(?:0[12]|1[013-8]|2[0-479]|5[125-8]|6[23679]|7[159]|8[01346]))\\d{5,8}|6(?:1(?:[0-8]\\d{4,7}|9\\d{4,8})|(?:[25]\\d|3[1-69]|4[1-6])\\d{5,8})|2(?:1(?:14|500)|2\\d{3})\\d{3}', example_number='218350123', possible_length=(7, 8, 9, 10, 11), possible_length_local_only=(5, 6)),
    mobile=PhoneNumberDesc(national_number_pattern='8[1-35-9]\\d{7,10}', example_number='812345678', possible_length=(9, 10, 11, 12)),
    toll_free=PhoneNumberDesc(national_number_pattern='(?:177\\d|800)\\d{5,7}', example_number='8001234567', possible_length=(8, 9, 10, 11)),
    premium_rate=PhoneNumberDesc(national_number_pattern='809\\d{7}', example_number='8091234567', possible_length=(10,)),
    shared_cost=PhoneNumberDesc(national_number_pattern='804\\d{7}', example_number='8041234567', possible_length=(10,)),
    uan=PhoneNumberDesc(national_number_pattern='(?:1500|8071\\d{3})\\d{3}', example_number='8071123456', possible_length=(7, 10)),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='8071\\d{6}', possible_length=(10,)),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['15']),
        NumberFormat(pattern='(\\d{2})(\\d{5,8})', format='\\1 \\2', leading_digits_pattern=['2[124]|[36]1'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{3})(\\d{5,7})', format='\\1 \\2', leading_digits_pattern=['800'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{5,8})', format='\\1 \\2', leading_digits_pattern=['[2-579]|6[2-5]'], national_prefix_formatting_rule='(0\\1)'),
        NumberFormat(pattern='(\\d{3})(\\d{3,4})(\\d{3})', format='\\1-\\2-\\3', leading_digits_pattern=['8[1-35-9]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{6,8})', format='\\1 \\2', leading_digits_pattern=['1'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{3})(\\d{4})', format='\\1 \\2 \\3', leading_digits_pattern=['804'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d)(\\d{3})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['80'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{4})(\\d{4,5})', format='\\1-\\2-\\3', leading_digits_pattern=['8'], national_prefix_formatting_rule='0\\1')])
