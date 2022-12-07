<template>
  
<div class="modal-bg">
  <div class="registerModal">
    <div class="modalContent">
      <div class="modalHeader">
        <h1>New Product Register</h1>
      </div>

      <form id="registerForm" @submit.prevent>
        <div class="modalBody">
        
          <div class="input-group mb-4">

            <label class="input-group-text" id="inputGroup-sizing-default" >Name</label>
            <input type="text" class="form-control" name="name" id="name" v-model="name">
          </div>
          <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default" >Category</label>
            <input type="text" class="form-control"  name="category" id="category" v-model="category">
          </div>

          <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default" >Unit</label>
            <input type="text" class="form-control" name="unit" id="unit" v-model="unit">
          </div>
          <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default" >Price</label>
            <input type="text" class="form-control" name="price" id="price" v-model="price">
          </div>
        </div>
        <div class="modalFooter">
          <button type="submit" class="btn btn-primary" @click="registerProduct()">Register</button>
          <button class="btn btn-secondary " @click="closeProductModal()">Close</button>
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
  name:"productRegister",
  computed:{
      ...mapState(['productModal','user']),
    },

  data(){
    return{
      errors:[],
      name:null,
      category:null,
      unit:null,
      price:null,
      
    }
  },

  methods:{
    ...mapMutations(['closeProductModal']),

    sendProdcutData(){
      axios.post('/api/product/registration',{
        name:this.name,
        category:this.category,
        unit:this.unit,
        price:this.price,
        coop:this.user.Coop_id,
      })
      .then(()=>{
        this.$emit('productRegister');
      })
      .catch((err)=>{
        console.error(err);
      })
    },

    registerProduct(){
      if(this.name && this.category && this.unit && this.price){
        this.sendProdcutData();
        return true;
      }
      this.errors = [];

      if(!this.name){
        this.errors.push('Name required');
      }

      if(!this.category){
        this.errors.push('category require');
      }
      // if(!this.phone){
      //   this.errors.push('id require');
      // }
      if(!this.unit){
        this.errors.push('unit require');
      }
      if(!this.price){
        this.errors.push('price require');
      }
      
      alert(this.errors);

    },
  }
}
</script>

<style>


</style>