<template>
<ProductRegister v-if="productModal == true" @productRegister="closeProductModal();getProductList();getQuantity()"/>

<div class="register">
  <table class="user-table">
    <caption>List of Product</caption>
    <thead >
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Category</th>
        <th scope="col">Unit</th>
        <th scope="col">Price</th>
        <th scope="col">Delete</th>
      </tr>
    </thead>
    <tbody>
      <tr class="memberList" scope="row" v-for="(item,i) in productList" :key="item" >
        <th scope="row">{{i+1}}</th>
        <td>{{item.Product_name}}</td>
        <td>{{item.Product_category}}</td>
        <td>{{item.Product_unit}}</td>
        <td>{{item.Product_price}}</td>
        <td><button type="button" class="btn btn-light" @click="deleteProduct(item.Product_id)">X</button></td>
      </tr>
    </tbody>
  </table>

  <div class="btBtn">
    <button type="button" class="btn btn-primary" @click="openProductModal()">
    New Product
    </button>
  </div>
</div>



</template>

<script>
import ProductRegister from '@/components/ProductRegister.vue';
import axios from 'axios'
import { mapActions, mapMutations, mapState } from 'vuex'
export default {
    name:'inventoryProduct',
    computed:{
      ...mapState(['productList','productModal']),
    },

    methods:{
      ...mapMutations(['closeProductModal','openProductModal']),
      ...mapActions(['getProductList','getQuantity']),
      deleteProduct(id){
        axios.delete(`/api/product/delete/${id}`)
        .then(()=>{
          this.getProductList();
          this.getQuantity();
        })
        .catch((err)=>{
          console.error(err);
        })
      },
    
    },
    components:{ProductRegister},
}
</script>

<style>

</style>