<template>

<shipmentRegister v-if="shipModal==true" @shipRegister="closeShipModal();getShipmentList();getQuantity();"/>

<div class="register">
  <div class="received-list">
    <table class="inven-table">
    <caption>Shipment</caption>
    <thead >
      <tr>
        <th scope="col">#</th>
        <th scope="col">Shipment Date</th>
        <th scope="col">Buyer</th>
        <th scope="col">Product</th>
        <th scope="col">Quantity</th>
        <th scope="col">Sales Price</th>
        <th scope="col">Delete</th>
      </tr>
    </thead>
    <tbody>
      <tr class="shipmentList" scope="row" v-for="(item,i) in shipmentList" :key="item" >
        <th scope="row">{{i+1}}</th>
        <td>{{item.Shipment_date.substr(0,10)}}</td>
        <td>{{item.Shipment_buyer}}</td>
        <td>{{item.Product_name}}</td>
        <td>{{item.Shipment_amount}}</td>
        <td>{{item.Shipment_price}}</td>
        <td><button class="btn btn-light" @click="deleteShipment(item.Shipment_id)">x</button></td>

      </tr>
    </tbody>

  </table>

  </div>
  
  <div class="inventory">
    <table class="inven">
      <caption>Total Quantity</caption>
      <thead >
        <tr>
          <th scope="col">#</th>
          <th scope="col">Product</th>
          <th scope="col">Current Quantity</th>
        </tr>
      </thead>
      <tbody>
        <tr scope="row" v-for="(item,i) in quantityList" :key="item">
          <th>{{i+1}}</th>
          <td>{{item.Product_name}}</td>
          <td>{{`${item.Warehousing_amount} ${item.Unit}`}}</td>
        </tr>
      </tbody>
    </table>
    <div class="inven-btn">
      <button type="button" class="btn btn-primary" @click="openShipModal()">
    New Shipment
    </button> 
    </div>
    
  </div>
</div>


</template>

<script>
import axios from 'axios'
import { mapActions, mapMutations, mapState } from 'vuex'
import shipmentRegister from '@/components/ShipmentRegister.vue'

export default {
  name: 'transactionShipment',
  computed: {
    ...mapState(['shipmentList','quantityList','shipModal']),
  },
  methods: {
    ...mapMutations(['openShipModal','closeShipModal']),
    ...mapActions(['getShipmentList','getQuantity']),
    deleteShipment(id){
      axios.delete(`/api/shipment/delete/${id}`)
      .then(()=>{
        this.getShipmentList();
        this.getQuantity();
      })
      .catch((err)=>{
        console.error(err);
      })
    },
  },
  components:{shipmentRegister}

}
</script>

<style>
.register{
  padding:20px;
  height: 100%;
  width: 100%;
  overflow: auto;
}

.ship{
  float: left;
  width:50%;
  height: 100%;
}
.quantity{
  float: left;
  width:50%;
  height: 100%;
}


</style>