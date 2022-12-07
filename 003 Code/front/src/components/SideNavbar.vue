<template>

<ul class="sidemenu" v-for="item in categoryData[category]" :key="item">
  <li class="sidemenu-list">
      <div class="sidemenu-item" @click="$router.push(`/${category}/${item.replace(/\s/gi,'-').toLowerCase()}`)" >{{item}}</div>
  </li>
</ul>


    

</template>

<script>
import { mapState } from 'vuex';
import categoryData from '../category';

export default {
    name:'SideNavbar',
    computed:{
      ...mapState(['category']),
      //computed 안에 mapState 로 가져오면 그냥변수처럼 사용가능
    },
    data(){
      return{
        categoryData:categoryData,
      }
    },
    methods:{

    },

}
</script>

<style>

.sidemenu{
  width:100%;
  text-align: center;
}
.sidemenu-list{
  padding-top: 30px;
  padding-bottom: 40px;
  flex-grow: 1;
  transition: 0.5s;
}

.sidemenu-item{
  cursor: pointer;
}
.sidemenu-list:hover{
  background-color: #9F73AB;
  flex-grow: 1.2;
}


</style>