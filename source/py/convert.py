def conv_header(df):
    # header칸의 타이틀 정보에 포함될 수 있는 정보 list
    template_header_list = [
        "학년",
        "반",
        "학교명",
        "학급 인원",
        "국어",
        "수학",
        "영어",
        "한국사",
        "탐구",
        "제2외국어/한문",
        "실시일"
    ]

    # header칸의 타이틀 정보를 포함할 list
    header_title_list = []

    # header칸의 내용 정보를 포함할 list
    header_text_list = []
    
    for i in df:
        for n in template_header_list:
            for j in df[i].values:
                if j == n:
                    # 타이틀 정보 append
                    header_title_list.append(j)
                    
                    # 내용 정보 append (타이틀에 대한 정보는 항상 2번 인덱스에 위치, dataframe image 참고)
                    header_text_list.append(df[i].values[2])
    
    return header_title_list, header_text_list

def conv_header_1st(df):
    # header칸의 타이틀 정보에 포함될 수 있는 정보 list
    template_header_list = [
        "학년",
        "반",
        "학교명",
        "학급 인원",
        "국어",
        "수학",
        "영어",
        "한국사",
        "사회",
        "과학",
        "실시일"
    ]

    # header칸의 타이틀 정보를 포함할 list
    header_title_list = []

    # header칸의 내용 정보를 포함할 list
    header_text_list = []
    
    for i in df:
        for n in template_header_list:
            for j in df[i].values:
                if j == n:
                    # 타이틀 정보 append
                    header_title_list.append(j)
                    
                    # 내용 정보 append (타이틀에 대한 정보는 항상 2번 인덱스에 위치, dataframe image 참고)
                    header_text_list.append(df[i].values[3])
    
    return header_title_list, header_text_list

def conv_header_sn(class_num, school_name):
    # header칸의 타이틀 정보를 포함할 list
    header_title_list = [
        "학년",
        "반",
        "학교명"
    ]

    # header칸의 내용 정보를 포함할 list
    header_text_list = [
        "3",
        class_num,
        school_name
    ]
    
    return header_title_list, header_text_list

def conv_content(df):
    # 영역 정보를 포함할 list
    content_top_title_list = []

    # 영역 정보를 얻기 위한 과정 (영역에 대한 정보는 항상 0번 인덱스에 위치, dataframe image 참고)
    for i in df.iloc[0]:
        # None이 아닌 값만 처리
        if i != None:
            # 공백 및 줄 바꿈 제거
            i_sub = i.replace(' ', '')
            i_sub = i_sub.replace('\n', '')

            # '영역'이라는 문자열이 포함된 내용만 처리
            if '영역' in i_sub:
                i_sub = i_sub.replace('영역', ' 영역')
                content_top_title_list.append(i_sub)
    
    # 성적 타이틀 정보를 포함할 list
    content_sub_title_list = ['번호', '성명']

    # 성적 타이틀 정보를 얻기 위한 과정 (성적 타이틀에 대한 정보는 항상 2번 인덱스에 위치, dataframe image 참고)
    for i in df.iloc[2]:
        # None이 아닌 값만 처리
        if i != None:
            # 줄 바꿈 제거
            i_sub = i.replace('\n', ' ')
            content_sub_title_list.append(i_sub)
    
    # 학생별 정보를 포함할 list
    content_text_list = []

    # df[3:-4] 범위를 한 개의 row씩 반복
    for idx, row in df[3:-4].iterrows():
        # 학생 수가 부족하여 한 페이지의 테이블을 다 채우지 못한 cell들은 ' '로 표기
        # 빈 cell인 경우에는 pass하고
        if row[0] == ' ':
            pass
        # 빈 cell이 아닌 경우에만 content list에 추가
        else:
            # 문자열은 str, 정수는 int, 실수는 float으로 처리하기 위한 작업
            # 하나의 row 별 list 생성
            content_text_list_sub = []

            # 하나의 row의 cell 수 반복
            for cell in row:
                # cell 값이 정수이면 int형으로 row 별 list에 추가
                if cell.isdigit():
                    content_text_list_sub.append(int(cell))
                
                else:
                    # cell 값이 실수이면 float형으로 row 별 list에 추가
                    if '.' in cell:
                        content_text_list_sub.append(float(cell))
                    
                    # cell 값이 문자열이면 str형으로 row 별 list에 추가 (기존 상태가 str)
                    else:
                        content_text_list_sub.append(cell)

            # row 별 list를 contnent list에 추가
            # content_text_list = [
            #    0번 row list,
            #    1번 row list,
            #    2번 row list,
            #    3번 row list,
            #    ...
            #    n번 row list,
            # ]
            content_text_list.append(content_text_list_sub)
        
    return content_top_title_list, content_sub_title_list, content_text_list

def conv_content_1st(df):
    # 영역 정보를 포함할 list
    content_top_title_list = []

    # 영역 정보를 얻기 위한 과정 (영역에 대한 정보는 항상 0번 인덱스에 위치, dataframe image 참고)
    for i in df.iloc[0]:
        # None이 아닌 값만 처리
        if i != None:
            # 공백 및 줄 바꿈 제거
            i_sub = i.replace(' ', '')
            i_sub = i_sub.replace('\n', '')

            # '영역'이라는 문자열이 포함된 내용만 처리
            if '영역' in i_sub:
                i_sub = i_sub.replace('영역', ' 영역')
                content_top_title_list.append(i_sub)
    
    del content_top_title_list[-1]
    content_top_title_list += ['사회', '과학', '국어 + 수학']
    
    # 성적 타이틀 정보를 포함할 list
    content_sub_title_list = ['번호', '성명']

    # 성적 타이틀 정보를 얻기 위한 과정 (성적 타이틀에 대한 정보는 항상 2번 인덱스에 위치, dataframe image 참고)
    for i in df.iloc[2]:
        # None이 아닌 값만 처리
        if i != None:
            # 줄 바꿈 제거
            i_sub = i.replace('\n', ' ')
            content_sub_title_list.append(i_sub)
    
    num = content_sub_title_list.pop()
    content_sub_title_list[-1] = f'백분율 (인원 : {num})'
    
    # 학생별 정보를 포함할 list
    content_text_list = []

    # df[3:-4] 범위를 한 개의 row씩 반복
    for idx, row in df.iloc[4:-4,:-1].iterrows():
        # 학생 수가 부족하여 한 페이지의 테이블을 다 채우지 못한 cell들은 ' '로 표기
        # 빈 cell인 경우에는 pass하고
        if row[0] == ' ':
            pass
        # 빈 cell이 아닌 경우에만 content list에 추가
        else:
            # 문자열은 str, 정수는 int, 실수는 float으로 처리하기 위한 작업
            # 하나의 row 별 list 생성
            content_text_list_sub = []
            
            # 하나의 row의 cell 수 반복
            for cell in row:
                # cell 값이 정수이면 int형으로 row 별 list에 추가
                if cell.isdigit():
                    content_text_list_sub.append(int(cell))
                
                else:
                    # cell 값이 실수이면 float형으로 row 별 list에 추가
                    if '.' in cell:
                        content_text_list_sub.append(float(cell))
                    
                    # cell 값이 문자열이면 str형으로 row 별 list에 추가 (기존 상태가 str)
                    else:
                        content_text_list_sub.append(cell)

            # row 별 list를 contnent list에 추가
            # content_text_list = [
            #    0번 row list,
            #    1번 row list,
            #    2번 row list,
            #    3번 row list,
            #    ...
            #    n번 row list,
            # ]
            content_text_list.append(content_text_list_sub)
            
    return content_top_title_list, content_sub_title_list, content_text_list

def conv_content_sn(df):
    # 영역 정보를 포함할 list
    content_top_title_list = [
        "한국사 영역", 
        "국어 영역", 
        "수학 영역", 
        "영어 영역", 
        "탐구 영역", 
        "제2외국어/한문"
    ]
    
    # 성적 타이틀 정보를 포함할 list
    content_sub_title_list = [
        '수험 번호', '성명',
        '등급',                                       # 한국사          2
        '선택 과목', '표준 점수', '백분위', '등급',   # 국어            3   ~ 
        '선택 과목', '표준 점수', '백분위', '등급',   # 수학            7   ~
        '등급',                                       # 영어            11
        '선택 과목', '표준 점수', '백분위', '등급',   # 탐구1           12  ~
        '선택 과목', '표준 점수', '백분위', '등급',   # 탐구2           16  ~
        '선택 과목','등급'                           # 제2외국어/한문  20 ~
    ]
    
    # 학생별 정보를 포함할 list
    content_text_list = []

    # df[3:-4] 범위를 한 개의 row씩 반복
    for idx, row in df.iterrows():
        if idx % 4 == 1: # 선택과목 row
            content_text_list_sub = content_sub_title_list.copy()

            row_sub_list = row[0].split('\n') # 수험번호, 성명, 생년월일
            student_num = row_sub_list[0] # 수험 번호
            student_name = row_sub_list[1] # 성명 , row_sub_list[2] = 생년월일 생략

            selected_korean = row[3]
            selected_math = row[4]

            selected_research_1 = row[6]
            selected_research_2 = row[7]
            selected_second_language = row[8]

            content_text_list_sub[0] = student_num
            content_text_list_sub[1] = student_name
            
            content_text_list_sub[3] = selected_korean
            content_text_list_sub[7] = selected_math
            
            content_text_list_sub[12] = selected_research_1
            content_text_list_sub[16] = selected_research_2
            content_text_list_sub[20] = selected_second_language # 제2외국어 누락 부분 수정
            
        elif idx % 4 == 0: # 등급 row
            rating_kor_history = row[2]
            rating_korean = row[3]
            rating_math = row[4]
            rating_english = row[4]
            rating_research_1 = row[6]
            rating_research_2 = row[7]
            rating_second_language = row[8]

            content_text_list_sub[2] = rating_kor_history
            content_text_list_sub[6] = rating_korean
            content_text_list_sub[10] = rating_math
            content_text_list_sub[11] = rating_english        
            content_text_list_sub[15] = rating_research_1
            content_text_list_sub[19] = rating_research_2
            content_text_list_sub[21] = rating_second_language

            content_text_list.append(content_text_list_sub)

        else:
            index_sub = idx % 4 # 2~3 row

            for_korean = row[3]
            for_math = row[4]

            for_research_1 = row[6]
            for_research_2 = row[7]

            content_text_list_sub[2 + index_sub] = for_korean
            content_text_list_sub[6 + index_sub] = for_math
            
            content_text_list_sub[11 + index_sub] = for_research_1
            content_text_list_sub[15 + index_sub] = for_research_2
        
    return content_top_title_list, content_sub_title_list, content_text_list

# 미사용 주석처리
# def conv_footer(df):
#     # set ROI for the footer
#     df.set_cropbox(fitz.Rect(0, 433, 841, 500)) # set a cropbox for the df
#     footer_text = df.get_text()
#     footer_text_list = footer_text.split("\n")
    
#     class_avg_kor = footer_text_list[4]
#     class_avg_math = footer_text_list[5]
#     class_avg_research = footer_text_list[6]

#     school_avg_kor = footer_text_list[8]
#     school_avg_math = footer_text_list[9]
#     school_avg_research = footer_text_list[10]
    
#     nw_avg_kor = footer_text_list[12]
#     nw_avg_math = footer_text_list[13]
#     nw_avg_research = footer_text_list[14]

#     footer_text_list = [
#         class_avg_kor,
#         class_avg_math,
#         class_avg_research,
#         school_avg_kor,
#         school_avg_math,
#         school_avg_research,
#         nw_avg_kor,
#         nw_avg_math,
#         nw_avg_research
#     ]

#     return footer_text_list