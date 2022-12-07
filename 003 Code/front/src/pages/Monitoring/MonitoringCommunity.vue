<template>

<WritePost v-if="postModal==true" @postRegister="closePostModal();getPostList()"/>
<div class="post-box">
<table class="post-table">
  <thead >
    <tr>
      <th scope="col">#</th>
      <th scope="col">Content</th>
      <th scope="col">Writer</th>
      <th scope="col">posting date</th>
    </tr>
  </thead>
  <tbody>
    <tr class="postList" scope="row" v-for="(item,i) in postList" :key="item" @click="$router.push(`/detail/${item.post_id}`)" >
      <th scope="row" class="post-num">{{i+1}}</th>
      <td class="post-text">{{item.text}}</td>
      <td class="post-author">{{item.author}}</td>
      <td class="post-date">{{item.post_date.substr(0,10)}}</td>
    </tr>
  </tbody>
</table>
</div >
<div class="postbtn"> 
  <button class="btn btn-primary" @click="openPostModal()">new post</button>
</div>

  
  
</template>

<script>
import WritePost from '@/components/WritePost.vue'

import { mapActions, mapMutations, mapState } from 'vuex'

export default {
  components: { WritePost },
  created(){
    this.setCommentList({})
  },
    computed:{
        ...mapState(['postList','postModal'])
    },
    methods:{
        ...mapMutations(['openPostModal','closePostModal']),
        ...mapActions(['getPostList',]),
        ...mapMutations(['setCommentList'])
    }
}

</script>

<style>
.post-table{
  margin:auto;
  width:1000px;
  font-size:10px;
  margin-top: 8px;
  text-align: center;
}

.post-num{
  width: 10px;
}
.post-text{
  width:600px;
}

.post-lost{
  height: 2rem;
}
.postbtn{
  text-align: right;
  margin-right: 150px;
}
</style>