<template>

<MemebrRegister v-if="memberModal==true" @memberRegister="closeMemberModal();getMemberList();"/>

<div class="register">
  <table class="user-table">
    <caption>List of Members</caption>
    <thead >
      <tr>
        <th scope="col">#</th>
        <th scope="col">Name</th>
        <th scope="col">Address</th>
        <th scope="col">phone</th>
        <th scope="col">Land Area</th>
        <th scope="col">Delete</th>
      </tr>
    </thead>
    <tbody>
      <tr class="memberList" scope="row" v-for="(item,i) in memberList" :key="item">
        <th scope="row">{{i+1}}</th>
        <td>{{item.Member_name}}</td>
        <td>{{item.Member_address}}</td>
        <td>{{item.Member_phone}}</td>
        <td>{{item.Member_area}}</td>
        <td><button type="button" class="btn btn-light" @click="deleteMember(item.Member_id)">X</button></td>
      </tr>
    </tbody>
  </table>
  <div class="btBtn">
    <button type="button" class="btn btn-primary" @click="openMemberModal()">
    New Member
    </button>
  </div>
  
</div>

</template>

<script>
import MemebrRegister from '@/components/MemberRegister.vue';
import axios from 'axios';
import { mapActions, mapMutations, mapState } from 'vuex';

export default {
    name: "coopRegister",
    computed:{
      ...mapState(['memberModal','memberList']),
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
.register{
  padding:20px;
  height: 100%;
  width: 100%;
  overflow: auto;
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