import sys

import pdfplumber
import pandas as pd
import dataframe_image as dfi

# PDF 파일에서 테이블을 추출할 때 입력하는 설정 list
# 공식 홈페이지 참고
table_settigs = {
    "vertical_strategy": "lines", 
    "horizontal_strategy": "lines",
    "explicit_vertical_lines": [],
    "explicit_horizontal_lines": [],
    "snap_tolerance": 3,
    "snap_x_tolerance": 3,
    "snap_y_tolerance": 3,
    "join_tolerance": 3,
    "join_x_tolerance": 3,
    "join_y_tolerance": 3,
    "edge_min_length": 3,
    "min_words_vertical": 1,
    "min_words_horizontal": 1,
    "text_tolerance": 3,
    "text_x_tolerance": 3,
    "text_y_tolerance": 3,
    "intersection_tolerance": 3,
    "intersection_x_tolerance": 3,
    "intersection_y_tolerance": 3,
}

def get_table_header(index, page):
    # 관심영역에서 테이블(표) 추출
    table = page.extract_table(table_settigs)
    
    # 추출한 테이블(표)로 데이터프레임 생성 
    df = pd.DataFrame(table)
    
    # 테이터프레임 이미지 저장
    dfi.export(df, f'./result/pdfplumber_test_image/df_image_{index}_header.png', max_cols = -1, max_rows = -1)

    # 데이터 프레임 반환
    return df

def get_table_content(index, page):
    # 관심영역에서 테이블(표) 추출
    table = page.extract_table(table_settigs)
    
    # 추출한 테이블(표)로 데이터프레임 생성 
    df = pd.DataFrame(table)
    
    # 테이터프레임 이미지 저장
    dfi.export(df, f'./result/pdfplumber_test_image/df_image_{index}_content.png', max_cols = -1, max_rows = -1)

    # 데이터 프레임 반환
    return df

def get_df_list(file_path):
    # PDF 파일 열기
    pdf = pdfplumber.open(file_path)

    # PDF 파일의 페이지 리스트 획득
    pages = pdf.pages
    # 반환할 데이터프레임 리스트 생성
    df_list = []

    # PDF 파일의 페이지 반복
    # 한 페이지에서 header와 content 구역을 따로 설정하여 두 개의 테이블을 추출
    for index, page in enumerate(pages):
        # header에 해당되는 테이블 추출
        df_header = get_table_header(index, page.crop((0,0,841,101)))
        
        # content에 해당되는 테이블 추출
        df_content = get_table_content(index, page.crop((0,105,841,595)))
        
        # [header, content] list 생성 (페이지 list)
        df_list_sub = [df_header, df_content]

        # [1 페이지 list, 2 페이지 list, 3 페이지 list, ... n 페이지 list]
        df_list.append(df_list_sub)
    
    # 데이터 프레임 반환
    # df list = [
    #    [1번 페이지 header, 1번 페이지 content],
    #    [2번 페이지 header, 2번 페이지 content],
    #    [3번 페이지 header, 3번 페이지 content],
    #    [4번 페이지 header, 4번 페이지 content],
    #    ...
    #    [n번 페이지 header, n번 페이지 content],
    # ]
    return df_list

def get_df_list_sn(file_path):
    # PDF 파일 열기
    pdf = pdfplumber.open(file_path)

    # PDF 파일의 페이지 리스트 획득
    pages = pdf.pages
    # 반환할 데이터프레임 리스트 생성
    df_list = []

    # PDF 파일의 페이지 반복
    # 한 페이지에서 header와 content 구역을 따로 설정하여 두 개의 테이블을 추출
    for index, page in enumerate(pages):
        width = page.bbox[2]
        height = page.bbox[3]
        # header에 해당되는 테이블 추출
        
        header = page.crop((width*0.05, 0, width*0.95, height*0.15)).extract_text()
        header_list = header.split()

        file_name = f"{header_list[0]} {header_list[1]} - {header_list[5]}"
        school_name = header_list[4]
        class_num = header_list[5][:-1]

        header_list_result = [file_name, school_name, class_num]
        
        # df_header = get_table_header(index, page.crop((width*0.05,height*0.1,width*0.95,height*0.3)))
        
        # content에 해당되는 테이블 추출
        df_content = get_table_content(index, page.crop((width*0.05, height*0.218, width*0.95, height*0.9)))
        if df_content.loc[0][0] == "":
            df_content.drop([0], axis=0, inplace=True)

        # [header, content] list 생성 (페이지 list)
        df_list_sub = [header_list_result, df_content]

        # [1 페이지 list, 2 페이지 list, 3 페이지 list, ... n 페이지 list]
        df_list.append(df_list_sub)
    
    # 데이터 프레임 반환
    # df list = [
    #    [1번 페이지 header, 1번 페이지 content],
    #    [2번 페이지 header, 2번 페이지 content],
    #    [3번 페이지 header, 3번 페이지 content],
    #    [4번 페이지 header, 4번 페이지 content],
    #    ...
    #    [n번 페이지 header, n번 페이지 content],
    # ]
    return df_list

if __name__ == '__main__':
    # print(get_df_list(sys.argv[1]))
    get_df_list_sn(sys.argv[1])