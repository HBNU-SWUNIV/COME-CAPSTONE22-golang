<template>
  
<div class="modal-bg">
  <div class="registerModal">
    <div class="modalContent">
      <div class="modalHeader">
        <h1>New Sales Register</h1>
      </div>

      <form id="registerForm" @submit.prevent>
        <div class="modalBody">
        
          <div class="input-group mb-4">
          
            <label class="input-group-text" id="inputGroup-sizing-default">Product</label>
            <select v-model="product">
              <option v-for="(item) in productList" :key="item" :value="item.Product_id">{{item.Product_name}}</option>
            </select>
            <label class="input-group-text" id="inputGroup-sizing-default" >Buyer</label>
            <input type="text" class="form-control"  name="buyer" id="buyer" v-model="buyer">
          </div>
          <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default" >Date</label>
            <input type="date" class="form-control"  name="date" id="date" v-model="date">
          </div>

          <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default" >Quantity</label>
            <input type="number" class="form-control" name="amount" id="amount" v-model="amount">
          </div>
          <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default" >Price</label>
            <input type="number" class="form-control" name="price" id="price" v-model="price">
          </div>
        </div>
        <div class="modalFooter">
          <button type="submit" class="btn btn-primary" @click="registerSales()">Register</button>
          <button class="btn btn-secondary " @click="closeSalesModal()">Close</button>
        </div>
      </form>

    </div>
  </div>
</div>

</template>
    
<script>
    import axios from 'axios';
    import { mapMutations, mapState } from 'vuex';
    
    
    export default {
      name:"salesRegister",
      computed:{
          ...mapState(['salesModal','productList']),
        },
    
      data(){
        return{
          errors:[],
          product:null,
          date:null,
          amount:null,
          price:null,
          buyer:null,
        }
      },
    
      methods:{
        ...mapMutations(['closeSalesModal']),
    
        sendSalesData(){
          axios.post('/api/sales/registration',{
            product: this.product,
            date: this.date,
            amount: this.amount,
            price: this.price,
            buyer:this.buyer,
          })
          .then(()=>{
            this.$emit('salesRegister');
          })
          .catch((err)=>{
            console.error(err);
          })
        },
    
        registerSales(){
          if(this.product && this.date && this.amount && this.price &&this.buyer){
            this.sendSalesData();
            return true;
          }
          this.errors = [];
    
          if(!this.product){
            this.errors.push('Product required');
          }
    
          if(!this.date){
            this.errors.push('date require');
          }

          if(!this.amount){
            this.errors.push('amount require');
          }
          if(!this.price){
            this.errors.push('price require');
          }
          if(!this.buyer){
            this.errors.push('buyer require');
          }
          
          alert(this.errors);
    
        },
      }
    }
    </script>
    
<style>
    
    
    </style>