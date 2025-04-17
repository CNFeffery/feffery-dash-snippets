# 这是一个快速生成fact在jupyter notebook中运行的模板（仅需修改数据和fact图表样式）

import dash
import feffery_antd_charts as fact
import random # 注意修改对应的数据

app = dash.Dash(__name__)

app.layout = fact.AntdLine( # 注意修改对应图表类型
    data=[
        {
            'date': f'2020-0{i}',
            'y': random.randint(50, 100),
        }
        for i in range(1, 10)
    ], # 注意修改对应数据
    xField='date',
    yField='y',
)

if __name__ == "__main__":
    app.run(jupyter='tab')