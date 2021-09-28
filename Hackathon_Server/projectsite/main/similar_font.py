#!/usr/bin/env python
# coding: utf-8

# ### 유사 폰트 뽑기 알고리즘(ver.0814)
# 
# 정리해주신 카테고리와 특성 값을 기준으로 알고리즘을 만들었습니다. 원리는 폰트가 주어지면 그 폰트의 특성 값과 기존에 있는 폰트들의 특성 값을 비교해서, 일치하면 1점씩 주게 됩니다. 기존에 있는 모든 폰트에 대해 점수를 매긴 다음, 점수 순위를 매겨서 top 4(자기 자신 포함 top 5)에 해당하는 유사 폰트를 뽑아줍니다. 주석을 달아놓는다고 달아놨는데 충분할 지 모르겠습니다. 혹시라도 궁금한 점 있으면 언제든 물어봐주세요!

# In[80]:


# 이 코드는 파이썬에서 데이터를 다루는 데 특화된 pandas 라이브러리를 활용합니다.
import pandas as pd


# In[81]:


# Mac과 Windows의 호환 차이로 encoding = 'cp949' 넣어주어야 합니다.
# .read_csv(경로)는 해당 경로에 있는 csv 파일을 pandas dataframe 형식으로 불러옵니다.
df = pd.read_csv('/workspace/git_repo/data.CSV',encoding='cp949')


# In[82]:


df


# In[83]:


# 이 데이터를 그대로 쓰기는 힘들기 때문에, 전처리 과정을 거쳐야 합니다. 인코딩 때문에 데이터가 온전치 못한 경우가 종종 있습니다.

## 데이터 전처리 1 : 필요한 Column만 뽑아내기
df_cleansing_1 = df[['폰트명','형태','무게감','유사한 인상 세트']]


# In[84]:


df_cleansing_1


# In[85]:


## 데이터 전처리 2 : 내용이 들어있는 행/열만 뽑아내기
## .isnull() : 결측치 여부 확인, .dropna() : 결측치 제거
df_cleansing_1.isnull()
df_cleansing_2 = df_cleansing_1.dropna()


# In[86]:


df_cleansing_2


# In[87]:


## 전처리 끝난 데이터프레임을 새로운 변수에 선언합니다.
df_new = df_cleansing_2


# ## 알고리즘을 어떻게 짤 것인가?
# 
# #### 제가 생각하면서 메모했던 내용들입니다.
# 
# 1) 어떻게 iterate를 시킬 것인가? 
# 
# 데이터 row 갯수만큼 처음부터 iterate를 시키면 된다.
# 
# 2) 어떻게 count를 매길 것인가?
# 
# 2-1) count column을 만들고
# 
# 2-2) 열 단위로 돌리면서
# 
# 2-3) count 값을 차례로 집어넣는다.
# 
# 3) count로 descending 정렬하고, 이후 자신 포함 상위 5개를 뽑으면 된다. 자신을 포함하는 이유는 알고리즘이 잘 돌아가는지 확인하기 용이하기 때문

# In[88]:


def return_similar_fonts(df, fontname):
    
    count_column = make_count_column(df, fontname) # 1) 2)를 한 번에 묶어서 만든 함수
    
    # 만들어진 count 열을 dataframe 뒤 쪽에 붙여서 새로운 dataframe을 만듭니다.
    
    df['count'] = count_column # df 뒤쪽에 열 추가
    df_sorted_by_value = df.sort_values(by ='count',ascending = False) # 내림차순 정렬
    top5_list = list(df_sorted_by_value.head()['폰트명']) # 상위 5개 값에서 폰트명 column을 리스트로 출력
    
    return top5_list ##결과를 보고 싶으면 이 블럭을 활성화하고,
    #return df_sorted_by_value ##검토를 해보고 싶으면 이 블럭을 활성화하시면 됩니다.
    
    
    
    


# In[89]:


# count 값들이 들어갈 list인 count_column을 만들어줍니다.

def make_count_column(df, fontname):
    
    count_column = [] # 빈 리스트 만들기
    
    fontname_idx = list(df['폰트명']).index(fontname) # 주어진 폰트명의 행 번호 찾기
    
    for idx in range(len(df.index)): # df의 행을 순회하면서
        
        count = 0 
        
        for column in df.columns: # df의 column 이름을 순회하면서
            
            if df[column][idx] == df[column][fontname_idx] : # 해당 column에서 주어진 폰트의 정보와 비교 폰트의 정보가 일치하면
                
                count += 1 # 1을 더해주기
        
        count_column.append(count) # 빈 리스트에 count 값을 추가해주기
        
    ## 여기까지 모든 행에 대해서 비교 작업을 마치고, count 값들이 매겨진 column이 완성됩니다.
    
    return count_column
        
        
        
        
        


# In[90]:


# 유사한 폰트 4개를 볼 수 있습니다.
# 해당 함수가 있는 코드블럭 참조
# [1:] 달아줘야 자기 자신은 제외하고 뽑힘
similar_list_top4 = return_similar_fonts(df_new,'SM3신신명조 03')[1:]
print(similar_list_top4)


# In[91]:


# 유사 폰트 상위 10개를 볼 수 있습니다. (데이터프레임을 보여주며, head안의 숫자를 조절해주면 원하는 갯수만큼 볼 수 있습니다)
# 해당 함수가 있는 코드블럭 참조
#return_similar_fonts(df_new,'J슈퍼맨M').head(10)


# In[ ]:




