<template>
<SalesRegister v-if="salesModal == true" @salesRegister="closeSalesModal();getSalesList();"/>

<div class="register">
  <table class="user-table">
    <caption>List of Sales</caption>
    <thead >
      <tr>
        <th scope="col">#</th>
        <th scope="col">Sales Date</th>
        <th scope="col">Buyer</th>
        <th scope="col">Product</th>
        <th scope="col">Amount</th>
        <th scope="col">Price</th>
        <th scope="col">Shipment</th>
        <th scope="col">Delete</th>
      </tr>
    </thead>
    <tbody>
      <tr class="salesList" scope="row" v-for="(item,i) in salesList" :key="item" >
        <th scope="row">{{i+1}}</th>
        <td>{{item.Sales_date.substr(0,10)}}</td>
        <td>{{item.Sales_buyer}}</td>
        <td>{{item.Product_name}}</td>
        <td>{{item.Sales_amount}}</td>
        <td>{{item.Sales_price}}</td>
        <td><button type="button" class="btn btn-light" @click="shipment(item.Sales_id)">Shipment</button></td>
        <td><button type="button" class="btn btn-light" @click="deleteSales(item.Sales_id)">X</button></td>
      </tr>
    </tbody>
  </table>

  <div class="btBtn">
    <button type="button" class="btn btn-primary" @click="openSalesModal()">
    New SalesRegister
    </button>
  </div>
</div>

</template>

<script>
import SalesRegister from '@/components/SalesRegister.vue';
import axios from 'axios'
import { mapActions, mapMutations, mapState } from 'vuex'

export default {

    name:'transactionSales',
    computed:{
      ...mapState(['salesList','salesModal','productList']),
    },
    methods:{
      ...mapMutations(['closeSalesModal','openSalesModal']),
      ...mapActions(['getSalesList','getShipmentList','getQuantity']),

      deleteSales(id){
        axios.delete(`/api/sales/delete/${id}`)
        .then(()=>{
          this.getSalesList();
        })
        .catch((err)=>{
          console.error(err);
        })
      },

      shipment(id){
        axios.get(`/api/sales/shipment/${id}`)
        .then(()=>{
          this.deleteSales(id);
          this.getShipmentList();
          this.getQuantity();
        })
        .catch((err)=>{
          console.error(err);
        })
      },
    },
    components:{SalesRegister}
}
</script>

<style>
.register{
  padding:20px;
  height: 100%;
  width: 100%;
  overflow: auto;
}

</style>