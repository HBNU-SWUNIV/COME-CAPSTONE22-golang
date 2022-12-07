<template>

  <body class="text-center">

    <div class="container">

      <div class="py-4 text-center">
        <h2>Sign up form</h2>
      </div>
      <div>
        <h4 class="mb-5">User Information</h4>
        <form class="needs-validation" @submit.prevent="signSubmit">

          <div class="mb-4">
            <label for="user name" class="form-label">Username</label>
            <div class="input-group has-validation">
              <input type="text" class="form-control" id="username" placeholder="Username" v-model="id">
              <div class="invalid-feedback">
                Your username is required.
              </div>
            </div>
          </div>

          <div class="mb-4">
            <label for="password" class="form-label">Password</label>
            <div class="input-group has-validation">
              <input type="text" class="form-control" id="password" placeholder="Password" v-model="password">
              <div class="invalid-feedback">
                Your password is required.
              </div>
            </div>
          </div>

          <div class="mb-4">
            <label for="cooperative" class="form-label">Cooperative </label>
            <input type="cooperative" class="form-control" id="cooperative" placeholder="cooperative name" v-model="coop">
            <div class="invalid-feedback">
              Please enter a your cooperative.
            </div>
          </div>

          <div class="mb-5">
            <label for="address" class="form-label">Address</label>
            <input type="text" class="form-control" id="address" placeholder="1234 Main St" v-model="address">
            <div class="invalid-feedback">
              Please enter your address.
            </div>
          </div>

          <button class="w-100 btn btn-primary btn-lg" type="submit">Sign Up!</button>

          <p class="mt-3 mb-3 text-muted">Return to <router-link to="/">Login</router-link>
          </p>

        </form>
      </div>
    </div>

  </body>

</template>
    
<script>
import axios from "axios";

export default {
  name: 'signUp',
  data() {
    return {
      id: null,
      password: null,
      coop: null,
      address: null
    }
  },
  methods: {
    signSubmit() {
      axios.post('/api/login/signUp',{
          id:this.id,
          password:this.password,
          coop:this.coop,
          address:this.address,
        })
        .then(()=>{
          this.$router.push({ name: "login" });
        })
        .catch((err)=>{
          console.error(err);
        });
    }
  }
}
</script>
    
<style scoped>
  
  body {
    display: flex;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
  }
  
  .container {
    max-width: 600px;
  }
  
  </style>