<template>
  <Line :chart-options="chartOptions" :chart-data="chartData" :chart-id="chartId" :plugins="plugins"
    :css-classes="cssClasses" :styles="styles" :width="1000" :height="400" />
</template>


<script>
import { Line } from 'vue-chartjs'
import axios from 'axios'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
)

export default {
  name: 'SimulateChart',
  components: {
    Line
  },
  props: {
    chartId: {
      type: String,
      default: 'line-chart'
    },
    width: {
      type: Number,
      default: 1000
    },
    height: {
      type: Number,
      default: 500
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => { }
    },
    plugins: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [{ data: [] }]
      },
      chartOptions: {
        responsive: false,
        maintainAspectRatio: false
      }
    }
  },
  methods: {
    setData() {
      // let id = this.$store.state.user.Coop_id;
      axios.get(`/api/monitoring/simulate`, { "Content-Type": "application-json" })
        .then((res) => {
          this.chartData = res.data;
        })
        .catch((err) => {
          console.error(err);
        })
    }
  },
  created() {
    this.setData()
  }
}

</script>


<style></style>