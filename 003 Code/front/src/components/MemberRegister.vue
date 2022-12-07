<template>
  
<div class="modal-bg">
  <div class="registerModal">
    <div class="modalContent">
      <div class="modalHeader">
        <h1>New Member Register</h1>
      </div>

      <form id="registerForm" @submit.prevent>
        <div class="modalBody">
        
          <div class="input-group mb-4">

            <label class="input-group-text" id="inputGroup-sizing-default" >Name</label>
            <input type="text" class="form-control" name="name" id="name" v-model="name">
            <label class="input-group-text" id="inputGroup-sizing-default" type="password" >Password</label>
            <input type="password" class="form-control" name="password" id="password" v-model="password">
          </div>
          
          <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default" >Phone Number</label>
            <input type="text" class="form-control"  name="phone" id="phone" v-model="phone">

            <label class="input-group-text" id="inputGroup-sizing-default" type="number" >Area</label>
            <input type="number" class="form-control" name="area" id="area" v-model="area">
          </div>

          <div class="input-group mb-4">
            <label class="input-group-text" id="inputGroup-sizing-default" >Address</label>
            <input type="text" class="form-control" name="address" id="address" v-model="address">
          </div>

        </div>
        <div class="modalFooter">
          <button type="submit" class="btn btn-primary" @click="registerMember()">Register</button>
          <button class="btn btn-secondary " @click="closeMemberModal()">Close</button>
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
  name:"memberRegister",
  computed:{
      ...mapState(['memberModal','user']),
    },

  data(){
    return{
      errors:[],
      name:null,
      id:null,
      address:null,
      phone:null,
      password:null,
      area:null,
    }
  },

  methods:{
    ...mapMutations(['closeMemberModal']),

    sendMemberData(){
      axios.post('/api/member/registration',{
        name:this.name,
        phone:this.phone,
        password:this.password,
        address:this.address,
        coop:this.user.Coop_id,
        area:this.area,
        
      })
      .then((response)=>{
        this.$emit('memberRegister');
        console.log(response)
      })
      .catch((err)=>{
        console.log(err);
      })
      

    },

    registerMember(){
    
      if(this.name && this.address && this.phone && this.password){
        this.sendMemberData();

        return true;
      }
      this.errors = [];

      if(!this.name){
        this.errors.push('Name required\n');
      }

      if(!this.address){
        this.errors.push('address require\n');
      }
      // if(!this.phone){
      //   this.errors.push('id require');
      // }
      if(!this.password){
        this.errors.push('password require');
      }
      
      alert(this.errors);

    },
  }
}
</script>

<style>
.modal-bg{
  position:fixed;
  width:90%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
}


.registerModal{
  width:70%;
  margin:80px auto;
  background:white;
  border-radius: 5px;
  padding: 20px 0;
}

.modalHeader{
  padding: 10px;
  border-bottom: solid 1px rgb(228, 222, 222);
  margin-bottom: 20px;
}

.modalBody{
  padding:5px;
}

.modalBody div{
  padding:5px;
}

.modalFooter{
  text-align: right;
}
.modalFooter button{
  margin-right: 5px;
}

</style>