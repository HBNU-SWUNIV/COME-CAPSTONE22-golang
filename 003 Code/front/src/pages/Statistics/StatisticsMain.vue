<template>
  <p>statistics main</p>
</template>

<script>
import axios from 'axios'

export default {

  name: 'statisticsMain',
  data() {
    return{
      engineGo: false,
      GoData: null
    }
  },
  methods: {
    engine() {
      this.engineGo = true
      const Go = this.engineGo
      axios.post(`/api/statistics/engine`, {Go})
        .then((res) => {
          this.GoData = res.data;
        })
        .catch((err) => {
          console.error(err);
        })
    }
  }
}
</script>

<style>

</style>