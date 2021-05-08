<template>
  <div>
    <div v-for="(item, index) in msg" :key="index">
      <div
        :id="'myChart' + index"
        :style="{ width: '1800px', height: '300px' }"
      ></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HellowWorld",
  async mounted() {
    this.msg = await this.getMessage("SensorInformation");
    this.$nextTick(() => {
      for (let index in this.msg) {
        console.log("myChart" + index);
        this.drawLine("myChart" + index, index);
      }
    });
  },
  data() {
    return {
      msg: "H",
    };
  },
  methods: {
    // axios实现前后端分离，在后端处理数据返回数据json，远程服务器使用本地环回地址0.0.0.0:5000
    // 需设置同步，异步会产生BUG
    async getMessage(path1) {
      let path = "/api/";
      path = path + path1;
      let res = await axios.get(path);
      return res.data;
    },
    // 对于图标进行信息注入与渲染
    async drawLine(id, index) {
      // 准备好的dom，建立echarts实例
      let myChart = this.$echarts.init(document.getElementById(id));
      // 绘制图表
      // 信息注入
      // X轴信息
      let x = this.msg[index].x;
      // Y轴信息
      let y = this.msg[index].y;
      // 标题信息
      let title = this.msg[index].title;
      console.log(x);
      myChart.setOption({
        title: { text: title },
        tooltip: {
          //悬浮窗信息设置
          formatter: "{b}, {a}:{c}" + this.msg[index].company,
        },
        xAxis: {
          //X轴信息
          data: x,
        },
        yAxis: {
          axisLabel: {
            //Y轴轴上信息
            formatter: (value) => value + this.msg[index].company,
          },
        },
        series: [
          {
            name: this.msg[index].name,
            //图类型
            type: "line",
            data: y,
          },
        ],
      });
    },
  },
};
</script>
