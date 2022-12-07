<template>

<div class="modal-bg">
    <div class="registerModal">
      <div class="modalContent">
        <div class="modalHeader">
          <h1>New Inventory Register</h1>
        </div>
  
        <form id="registerForm" @submit.prevent>
          <div class="modalBody">
            <div class="input-group mb-4">  
              <label class="input-group-text" id="inputGroup-sizing-default" >Product</label>
              <select v-model="product">
                <option v-for="(item) in productList" :key="item" :value="item.Product_id">{{item.Product_name}}</option>
              </select>
              <label class="input-group-text" id="inputGroup-sizing-default" >Member</label>
              <select v-model="member">
                <option>None</option>
                <option v-for="(item) in memberList" :key="item" :value="item.Member_id">{{item.Member_name}}</option>
              </select>

            </div>

            <div class="input-group mb-4">
              <label class="input-group-text" id="inputGroup-sizing-default" >Quantity</label>
              <input type="number" min="0" class="form-control" name="amount" id="amount" v-model="amount">
            </div>

            <div class="input-group mb-4">
              <label class="input-group-text" id="inputGroup-sizing-default" >Received Date</label>
              <input type="date" class="form-control" name="date" id="date" required pattern="\d{4}-\d{2}-\d{2}" v-model="date">
            </div>

            <div class="input-group mb-4">
              <label class="input-group-text" id="inputGroup-sizing-default" >Price</label>
              <input type="number" min="0" class="form-control" name="price" id="price" v-model="price">
            </div>

            <div class="input-group mb-4">
              <label class="input-group-text" id="inputGroup-sizing-default" >Quality</label>
              <input type="text" class="form-control" name="quality" id="quality" v-model="quality">
            </div>
          </div>
          <div class="modalFooter">
            <button type="submit" class="btn btn-primary" @click="registerInventory()">Register</button>
            <button class="btn btn-secondary " @click="closeInventoryModal()">Close</button>
          </div>
        </form>
      </div>
    </div>
  </div>

</template>

<script>
import { mapActions, mapMutations, mapState } from 'vuex'
import axios from 'axios'

export default {
    name:'inventoryRegister',
    computed:{
        ...mapState(['inventoryModal','productList','memberList','user','todayDate'])
    },
    methods:{
        ...mapMutations(['closeInventoryModal']),
        ...mapActions(['getQuantity']),

        sendInventoryData(){
        
        axios.post(`/api/inventory/registration/${this.user.Coop_id}`,{
          member : this.member,
          product : this.product, 
          amount : this.amount,
          date : this.date,
          price : this.price,
          quality : this.quality,
          
        })
        .then(()=>{
            this.$emit('inventoryRegister');
        })
        .catch((err)=>{
          console.error(err);
        })
      },
  
      registerInventory(){
        if(this.member && this.product && this.amount && this.date && this.price && this.quality){

          this.sendInventoryData();
          return true;
        }

        this.errors = [];

        if(!this.member){
          this.errors.push(' member required');
        }
        if(!this.product){
          this.errors.push(' product required');
        }
        if(!this.amount){
          this.errors.push(' amount required');
        }
        if(!this.date){
          this.errors.push(' date required');
        }
        if(!this.price){
          this.errors.push(' price required');
        }
        if(!this.quality){
          this.errors.push(' quality required');
        }

        alert(this.errors);
  
      },
    },
    data(){
        return{
            errors:[],
            member:null,
            product:null,
            amount:null,
            date:null,
            price:null,
            quality:null,
            
        }
    },
}
</script>

<style>

</style>