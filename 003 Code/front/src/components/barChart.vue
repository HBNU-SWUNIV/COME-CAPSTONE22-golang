<template>
    <Bar :chart-options="chartOptions" :chart-data="chartData" :chart-id="chartId" :plugins="plugins"
        :css-classes="cssClasses" :styles="myStyles" :width="1000" :height="400" />
</template>
  
<script>
import { Bar } from 'vue-chartjs'
import axios from 'axios'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    name: 'BarChart',
    components: { Bar },
    props: {
        chartId: {
            type: String,
            default: 'bar-chart'
        },
        datasetIdKey: {
            type: String,
            default: 'label'
        },
        width: {
            type: Number,
            default: 400
        },
        height: {
            type: Number,
            default: 400
        },
        cssClasses: {
            default: '',
            type: String
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
            }
        }
    },
    methods: {
        setData() {
            let id = this.$store.state.user.Coop_id;
            const form = 'price'
            axios.post(`/api/statistics/month/${id}`, { form }, { "Content-Type": "application-json" })
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

<style>

</style>