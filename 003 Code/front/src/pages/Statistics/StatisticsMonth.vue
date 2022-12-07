<template>
  <h1>Statistics Month</h1>
  <Line />
  <bar />

  

</template>
  
<script>
import Line from '@/components/LineChart.vue'
import bar from '@/components/barChart.vue'


export default {
  components: { Line, bar },
  name: 'statisticsMonth',
  data() {
    return {

    }
  },
}
</script>
  
<style>
.bar-chart{
  width: 50%;
  max-height: 300px;
}
</style>