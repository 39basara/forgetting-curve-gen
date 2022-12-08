import numpy as np
import matplotlib as mpl
mpl.use('Agg') # この行を追記
import matplotlib.pyplot as plt

# arg
hour = 24
minute = 60


#　復習回数と経過時間を指定するとその経過時間時点での忘却率を返す
def gen_recallrate_by_times(recall_time,passed_hour):
    # args= [1,5,15,50,500,5000]
    args= [1,5,15,50,300,1500]
    rate=np.e**(-(passed_hour)/(args[recall_time]*hour))
    return 1-rate

#　学習時間を入れると、自動で復習のタイミングで必要な復習時間を返す
def make_auto_schedule(learn_time):
    auto_passed_hour=[8,24,72,168,296,720]
    schedule_list={}
    for i,passed_hour in enumerate(auto_passed_hour):
        rate = gen_recallrate_by_times(i,passed_hour)
        recall_time = learn_time*rate
        # schedule_list[i+1]=recall_time
        schedule_list[auto_passed_hour[i]]=recall_time
    return schedule_list

# 忘却曲線のシミュレーター
def gen_forgetting_curve_simulator():
    # 整備中
    # [仮]グラフ生成時の引数。値は復習した時の前の学習時間からの経過時間を入力。
    recall_1 = 12
    recall_2 = 24
    recall_3 = 48
    recall_4 = 72
    recall_5 = 168
    recall_6 = 296
    margin = 100
    display_hour = round(recall_1+recall_2+recall_3+recall_4 +recall_5+recall_6+margin,-2)
    # forgetting curve with revival bar
    # x is an arrange for displaying the graph with the length of actual recall date
    # x1 is an arrange for displaying the graph of future recall rate 
    x = np.arange(0, display_hour)
    x1 = np.arange(0, recall_1)

    xx = np.arange(0, display_hour-recall_1)
    x2 = np.arange(0, recall_2)

    xxx = np.arange(0, display_hour-recall_1-recall_2)
    x3 = np.arange(0, recall_3)
    
    xxxx = np.arange(0, display_hour-recall_1-recall_2-recall_3)
    x4 = np.arange(0, recall_4)
    
    xxxxx = np.arange(0, display_hour-recall_1-recall_2-recall_3-recall_4)
    x5 = np.arange(0, recall_5)
    
    xxxxxx = np.arange(0, display_hour-recall_1-recall_2-recall_3-recall_4-recall_5)
    x6 = np.arange(0, recall_6)

    # xxxxxxx = np.arange(0, display_hour-recall_1-recall_2-recall_3-recall_4-recall_5-recall_6)
    # x6 = np.arange(0, recall_6)


    # # forgetting curve based on ebinghaus 1897
    # # 学術的に不正確。興味ない古文の単語の暗記とかように使えるからコメントアウト
    # with np.errstate(divide='ignore', invalid='ignore'):
    #     R0=1.84/(np.log10(1*60*x)**1.25+1.84)
    # R0[0]=1
    # plt.plot(x, 1-R0, color = "green", linestyle = ":")

    # R is an equasion for displayig actual recall rate by bar graph
    # R_if is an equasion for displayigfuture recall rate by plotqwqwq
    R1=gen_recallrate_by_times(0,x1)
    R1_if=gen_recallrate_by_times(0,x)

    R2=gen_recallrate_by_times(1,x2)
    R2_if=gen_recallrate_by_times(1,xx)

    R3=gen_recallrate_by_times(2,x3)
    R3_if=gen_recallrate_by_times(2,xxx)

    R4=gen_recallrate_by_times(3,x4)
    R4_if=gen_recallrate_by_times(3,xxxx)

    R5=gen_recallrate_by_times(4,x5)
    R5_if=gen_recallrate_by_times(4,xxxxx)

    R6=gen_recallrate_by_times(5,x6)
    R6_if=gen_recallrate_by_times(5,xxxxxx)


    #描画パート
    # barは棒グラフ、
    # plotは点グラフ
    plt.bar(x1, R1, color = "red", linestyle = "--")
    plt.plot(x, R1_if, color = "red", linestyle = "--")

    plt.bar(x2+recall_1, R2, color = "blue", linestyle = "solid")
    plt.plot(xx+recall_1, R2_if, color = "blue", linestyle = "--")

    plt.bar(x3+recall_1+recall_2, R3, color = "green", linestyle = "dashed")
    plt.plot(xxx+recall_1+recall_2, R3_if, color = "green", linestyle = "dashed")

    plt.bar(x4+recall_1+recall_2+recall_3, R4,  color = "blue", linestyle = ":")
    plt.plot(xxxx+recall_1+recall_2+recall_3, R4_if,  color = "blue", linestyle = ":")

    plt.bar(x5+recall_1+recall_2+recall_3+recall_4, R5,  color = "red", linestyle = ":")
    plt.plot(xxxxx+recall_1+recall_2+recall_3+recall_4, R5_if,  color = "red", linestyle = ":")

    plt.bar(x6+recall_1+recall_2+recall_3+recall_4+recall_5, R6,  color = "green", linestyle = ":")
    plt.plot(xxxxxx+recall_1+recall_2+recall_3+recall_4+recall_5, R6_if,  color = "green", linestyle = ":")

    # サイズや軸ラベルの調整
    plt.ylim([0,1.02])
    plt.rcParams["figure.figsize"] = (800, 640)
    plt.xlabel("passed hours")
    plt.ylabel('nessesary time to recall')
    plt.grid()
    # plt.legend()
    # グラフを描画してファイルに保存する処理
    plt.savefig("hoge.png") 
    print("グラフの生成が完了しました。")


        

def main():
    task_hour = 20
    print(f"学習に{task_hour}時間かかったタスクの復習計画の生成完了")
    result = make_auto_schedule(task_hour)
    # print(result)
    aaa = 0
    times=0
    for times,recall_hour in result.items():
        times+=times
        print(f"{times}時間後の復習にかかる時間は{round(recall_hour,1)}時間です。")
        aaa+=recall_hour
    print(f"合計復習時間は{round(aaa)}時間になります。１月後の忘却率は{round(gen_recallrate_by_times(5,720)*100,2)}%です。")
    oneday_recall_rate = round(gen_recallrate_by_times(0,24),4)
    print(f"もし一夜漬けで対処した場合は、２４時間後の忘却率は{oneday_recall_rate*100}%なので、前日に{task_hour}時間かけて獲得した知識は{round(task_hour*(1-oneday_recall_rate))}時間分しか残りません。")
    gen_forgetting_curve_simulator()





    # print(gen_recallrate_by_times(0,x1))

main()

# def calc_relearn_time(learn_time,learn_date):
#     recall_time1,recall_time2,recall_time3,recall_time4,recall_time5


# TODO 
# パーセントから時間の表記にする
# Recallの回数によって最終ラインの描画を変更OR大木い画像を出力できるように
# 上のやつを結集した値を出して年間計画を作れるように
# スケジュール帳に自動で間隔学習のスケジュールもいれ、その場合の総勉強時間も作る
# 間違ったタイミングでの復習をした場合と比べて、どれだけ得したか魅せる
# とりぜずDBの代わりにCSVで保存
# 日にち・時間表示・変更機能

