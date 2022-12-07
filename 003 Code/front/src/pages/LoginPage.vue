<template>

  <body class="text-center">

    <main class="form-signin w-100 m-auto">
      <form @submit.prevent>
        <h2 class="mb-5 fw-normal">Please sign in</h2>

        <div class="form-floating">
          <input type="id" class="form-control" id="id" placeholder="username" v-model="id">
          <label for="loginId">User name</label>
        </div>
        <div class="form-floating">
          <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
          <label for="loginPw">Password</label>
        </div>

        <div class="checkbox mb-3">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
        <button class="w-100 btn btn-lg btn-primary" type="submit" @click="onSubmit">Sign in</button>
        <p class="mt-3 mb-3 text-muted">If you don't have an account, please proceed with the <router-link to="/signup">
            Sign up</router-link> first!</p>
        <div>
          <p class="mt-3 mb-3 text-muted">You can preview the <router-link to="/home">InventoryPage</router-link>
          </p>
        </div>
        
      </form>
    </main>

  </body>
</template>

<script>
import axios from "axios";
import { mapActions } from 'vuex';

export default {
  name: 'loginPage',
  data() {
    return {
      id: null,
      password: null
    }
  },
  methods: {
    ...mapActions(['getUserInfo']),
    onSubmit() {
      const id = this.id;
      const password = this.password;
      
      axios.post("api/login/signIn", { id, password }, { "Content-Type": "application-json" })
        .then((res) => {

          if (res.data.user) {
            this.$store.commit("setUser", res.data.user);
            // this.getUserInfo();
            this.$router.push({ name: "home" });
          } else if (res.data.message) {
            alert(res.data.message);
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    login() {
      this.$router.replace('/')
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

.form-signin {
  max-width: 330px;
  padding: 15px;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-signin input[type="id"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

</style>