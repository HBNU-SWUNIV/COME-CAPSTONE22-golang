<template>
<WarehousingRegister v-if="warehousingModal == true" @warehousingRegister="closeWarehousingModal(); getWarehousing();getQuantity(); getManage();"/>

<div>
  <table class="user-table">
    <caption>Warehousing schedule</caption>
    <thead >
      <tr>
        <th scope="col">#</th>        
        <th scope="col">Product</th>
        <th scope="col">quantity</th>
        <th scope="col">member name</th>
        <th scope="col">request price</th>
        <th scope="col">schedule</th>
        <th scope="col">quailty</th>
        <th scope="col">warehousing</th>
        <th scope="col">delete</th>
      </tr>
    </thead>
    <tbody>
      <tr class="warehousingList" scope="row" v-for="(item,i) in warehousingList" :key="item">
        <th scope="row">{{i+1}}</th>
        <td>{{item.Product_name}}</td>
        <td>{{item.Shipment_amount}}</td>
        <td>{{item.Member_name}}</td>
        <td>{{item.Req_price}}</td>
        <td>{{item.Shipment_date.substr(0,10)}}</td>
        <td>{{item.Product_quailty}}</td>
        <td><button @click="received(item.Schedule_id)" type="button" class="btn btn-light">Received</button></td>
        <td><button type="button" class="btn btn-light" @click="deleteWarehousing(item.Schedule_id)">X</button></td>
      </tr>
    </tbody>
  </table>

  <div class="btBtn">
    <button type="button" class="btn btn-primary" @click="openWarehousingModal()">
    New Warehousing
    </button>
  </div>
</div>

</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex'
import WarehousingRegister from '@/components/WarehousingRegister.vue'
import axios from 'axios'

export default {
    name: "inventoryStatus",
    computed:{
      ...mapState(['warehousingModal','warehousingList','memberList','productList'])
    },
    methods: {
        ...mapMutations(["openWarehousingModal","closeWarehousingModal"]),
        ...mapActions(['getWarehousing','getReceived','getQuantity','getManage']),

        deleteWarehousing(id){
        axios.delete(`/api/warehousing/delete/${id}`)
        .then(()=>{
          this.getWarehousing();
          this.getQuantity();
          this.getManage();
        })
        .catch((err)=>{
          console.error(err);
        })
      },
      received(id){
        axios.get(`/api/warehousing/received/${id}`)
        .then(()=>{
          this.deleteWarehousing(id);
          this.getReceived();
          this.getManage();
        })
        .catch((err)=>{
          console.error(err);
        })
        //warehousing schedule 들어가서 received 를 true 로 바꾸는코드
      }
    },
    components: { WarehousingRegister }
    ,

}
</script>

<style>

</style>