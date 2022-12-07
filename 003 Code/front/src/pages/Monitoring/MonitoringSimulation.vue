<template>

    <div class="simulation-input">

        <div class="input-group mt-4 mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default">Storage period</label>
            <input type="number" min="0" class="form-control" name="storagePeroid" id="storagePeroid"
                v-model="storagePeriod">
        </div>

        <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default">Expected change in demand</label>
            <span class="input-group-text">+</span>
            <input type="number" min="0" class="form-control" name="demand" id="demand" v-model="demand">
            <span class="input-group-text">%</span>
        </div>

        <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default">Expected change in supply</label>
            <span class="input-group-text">+</span>
            <input type="number" min="0" class="form-control" name="afterSowing" id="supply" v-model="supply">
            <span class="input-group-text">%</span>
        </div>

        <button class="btn btn-primary" type="button" @click="simulationStart">Simulation</button>

    </div>


    <div class="sim-result">
        <h1>Simulation Result</h1>
        <Line v-if="loaded" :chart-data="chartData" :width="1000" :height="400" />
    </div>


</template>

<script>
import axios from 'axios'
import { Line } from 'vue-chartjs'

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
    name: "monitoringSimulation",
    components: { Line },
    data() {
        return {
            storagePeriod: null,
            demand: null,
            supply: null,
            engineGo: true,
            GoData: null,
            Data: null,
            loaded: false,
            chartData: {
                labels: [],
                datasets: [{ data: [] }]
            },
        }
    },
    methods: {
        simulationStart() {
            const period = this.storagePeriod
            const demand = this.demand
            const supply = this.supply
            axios.post(`/api/monitoring/simulate`, { period, demand, supply })
                .then((res) => {
                    this.GoData = res.data;
                    this.setData()
                })
                .catch((err) => {
                    console.error(err);
                })
        },
        setData() {
            axios.get(`/api/monitoring/simulate`, { "Content-Type": "application-json" })
                .then((res) => {
                    this.chartData = res.data;
                })
                .catch((err) => {
                    console.error(err);
                })
        }
    },
    async mounted() {
        this.loaded = false

        try {
            axios.get(`/api/monitoring/simulate`, { "Content-Type": "application-json" })
                .then((res) => {
                    this.chartData = res.data;
                })
                .catch((err) => {
                    console.error(err);
                })

            this.loaded = true
        } catch (e) {
            console.error(e)
        }
    },
    created() {
        this.setData()
    }
}
</script>

<style>
.simulation-input {
    padding: 10px;
    width: 50%;
    margin-left: 100px;
}

.sim-result {
    padding: 15px;
    margin-left: 100px;
    width: 70%;
}
</style>