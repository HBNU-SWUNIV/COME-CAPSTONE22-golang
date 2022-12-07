<template>
  <div class="top">
    <TopNavbar></TopNavbar>
  </div>
  <div class="main">
    <div class="sidebar">
        <side-navbar></side-navbar>
    </div>
    <div class="mainPage">
        <router-view></router-view>
    </div>
  </div>



</template>

<script>
import SideNavbar from '@/components/SideNavbar.vue';
import TopNavbar from '@/components/TopNavbar.vue';

export default {
    components: { SideNavbar, TopNavbar },

}
</script>

<style>


.top{
  width: 100%;
  height: 55px;
  min-width: z1000px;
}
.main{
  width:100%;
  min-width: 1000px;
  height: calc(100% - 55px);
  height : -webkit-calc(100% - 55px); /* for Chrome, Safari */ 
  height : -moz-calc(100% - 55px); /* for Firefox */
  clear: both;

}

.sidebar{
  min-width: 100px;
  float: left;
  width: 10%;
  height:100%;
  background: #624F82;
  color: #eee;
  font-size: 12px;
  
}
.mainPage{
  width:90%;
  min-width: 880px;
  /* height: calc(100% - 50px);
  height : -webkit-calc(100% - 50px);
  height : -moz-calc(100% - 50px);  */
  float: left;
  overflow: auto;
  height: 100%;
}

</style>