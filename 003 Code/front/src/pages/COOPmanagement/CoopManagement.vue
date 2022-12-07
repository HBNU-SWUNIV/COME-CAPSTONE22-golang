<template>

  <MemebrRegister v-if="memberModal==true" @memberRegister="closeMemberModal();getMemberList();"/>
  
  <div class="manage">
    <table class="manage-table">
      <caption>Coop Infomation</caption>
      <thead >
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
        </tr>
      </thead>
      <tbody>
        <tr class="memberList" scope="row" >
          <th scope="row">name</th>
          <td>{{user.Coop_name}}</td>
        </tr>
        <tr>
          <th scope="row">address</th>
          <td>{{user.Coop_address}}</td>
        </tr>

      </tbody>
    </table>
    
  </div>
  <div>
    <table class="manage-table">
      <caption>List of Members</caption>
      <thead >
        <tr>
          <th scope="col">#</th>
          <th scope="col">Name</th>
          <th>Expected warehousing date</th>
          <th>Recent Updates</th>
        </tr>
      </thead>
      <tbody>
        <tr class="memberList" scope="row" v-for="(item,i) in manageList" :key="item">
          <th scope="row">{{i+1}}</th>
          <td>{{item.Member_name}}</td>
          <td>{{item.shipment_date}}</td>
          <td>{{item.update_date}}</td>
        </tr>
      </tbody>
    </table>
  </div>

  
  </template>
  
  <script>
  import MemebrRegister from '@/components/MemberRegister.vue';
  import axios from 'axios';
  import { mapActions, mapMutations, mapState } from 'vuex';
  
  export default {
      name: "coopRegister",
      computed:{
        ...mapState(['manageList','memberList','user']),
      },
      methods:{
        ...mapMutations(['closeMemberModal','openMemberModal']),
        ...mapActions(['getMemberList']),
  
        deleteMember(id){
          axios.delete(`/api/member/delete/${id}`)
          .then(()=>{
            this.getMemberList();
          })
          .catch((err)=>{
            console.error(err);
          })
        }
      },
      components: { MemebrRegister }
  }
  </script>
  
  <style>
.manage{
  float: left;
  width:30%;
  margin-left: 50px;
}
  caption{
    caption-side: top
  }
  td,th{
    padding:5px;
    border-bottom: 1px solid #f2f2f2;
  }
  .user-table{
    background-color: transparent;
    width:900px;
    margin:auto;
  }

  .btBtn{
    text-align: center;
    margin-top: 20px;
    margin-left: 700px;
    
  }
  
  </style>