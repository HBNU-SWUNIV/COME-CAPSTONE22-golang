// import axios from 'axios'
import axios from 'axios';
import { createStore } from 'vuex'
// import axios from 'axios'

let today = new Date();

let year = today.getFullYear(); // 년도
let month = today.getMonth() + 1;  // 월
let date = today.getDate();  // 날짜

let todayDate = `${year}-${month}-${date}`
const store = createStore({

    state(){
        return{
            //데이터 여기에 보관하기 vuex
            category:'',
            memberModal:false,
            productModal:false,
            warehousingModal:false,
            shipModal:false,
            salesModal:false,
            inventoryModal:false,
            postModal:false,
            productList:{},
            memberList:{},
            salesList:{},
            warehousingList:{},
            shipmentList:{},
            user: null,
            receivedList:{},
            quantityList:{},
            postList:{},
            commentList:{},
            manageList:{},
            todayDate: todayDate,



        }
    },
    getters: {
        user: (state) => { return state.user; }
    },
    mutations: {
        //state변경 함수를 정의
        userSelect(state, payload) {
            state.category = payload;
        },
        openMemberModal(state) {
            state.memberModal = true;
        },
        closeMemberModal(state) {
            state.memberModal = false;
        },
        openProductModal(state) {
            state.productModal = true;
        },
        closeProductModal(state) {
            state.productModal = false;
        },
        openWarehousingModal(state) {
            state.warehousingModal = true;
        },
        closeWarehousingModal(state) {
            state.warehousingModal = false;
        },

        openPostModal(state){
            state.postModal = true
        },
        closePostModal(state){
            state.postModal = false
        },
        openSalesModal(state){
            state.salesModal=true;

        },
        closeSalesModal(state) {
            state.salesModal = false;
        },
        openInventoryModal(state) {
            state.inventoryModal = true;
        },
        closeInventoryModal(state) {
            state.inventoryModal = false;

        },

        openShipModal(state){
            state.shipModal = true;
        },
        closeShipModal(state){
            state.shipModal = false;
        },
        setProductList(state,payload){

            state.productList = payload;
        },
        setMemberList(state, payload) {
            state.memberList = payload;
        },
        setWarehousingList(state, payload) {
            state.warehousingList = payload;
        },
        setSalesList(state, payload) {
            state.salesList = payload;
        },
        setShipmentList(state, payload) {
            state.shipmentList = payload;
        },
        setUser(state, user) {
            state.user = user;
        },
        setReceivedList(state, payload) {
            state.receivedList = payload;
        },
        setQuantityList(state, payload) {
            state.quantityList = payload;
        },

        setPostList(state,payload){
            state.postList = payload;
        },
        setCommentList(state,payload){
            state.commentList = payload;
        },
        setManage(state,payload){
            state.manageList=payload;
        }

    },
    actions: {

        //ajax와같이 시간걸리는것
        getProductList(context) {
            let id = context.state.user.Coop_id;
            axios.get(`/api/product/data/${id}`,
            )
                .then((res) => {
                    context.commit('setProductList', res.data);
                })
                .catch((err) => {
                    console.error(err);
                })
        },

        getMemberList(context) {
            let id = context.state.user.Coop_id;
            axios.get(`/api/member/data/${id}`)
                .then((res) => {
                    context.commit('setMemberList', res.data);
                    console.log();

                })
                .catch((err) => {
                    console.error(err);
                })
        },

        getWarehousing(context) {
            let id = context.state.user.Coop_id;
            axios.get(`/api/warehousing/stock/${id}`)
                .then((res) => {

                    context.commit('setWarehousingList', res.data);
                })
                .catch((err) => {
                    console.error(err);
                });
        },


        getSalesList(context) {
            let id = context.state.user.Coop_id;
            axios.get(`/api/sales/data/${id}`)
                .then((res) => {
                    context.commit('setSalesList', res.data);
                })
                .catch((err) => {
                    console.error(err);
                })
        },

        getReceived(context) {
            let id = context.state.user.Coop_id;
            axios.get(`/api/inventory/received/${id}`)
                .then((res) => {
                    context.commit('setReceivedList', res.data);

                })
                .catch((err) => {
                    console.error(err);
                })
        },

        getShipmentList(context) {
            let id = context.state.user.Coop_id;
            axios.get(`/api/shipment/data/${id}`)
                .then((res) => {
                    context.commit('setShipmentList', res.data);
                })
                .catch((err) => {
                    console.error(err);
                })

        },
        getPostList(context){
            let id = context.state.user.Coop_id
            axios.get(`/api/community/post/${id}`)
            .then((res)=>{
                context.commit('setPostList',res.data)
            })
            .catch((err)=>{
                console.error(err);
            })
        },
        getCommentList(context,id){
            axios.get(`/api/community/comment/${id}`)
            .then((res)=>{
                context.commit('setCommentList',res.data)
            })
            .catch((err)=>{
                console.error(err)
            })
        },

        getQuantity(context) {
            let id = context.state.user.Coop_id;
            axios.get(`/api/inventory/quantity/${id}`)
                .then((res) => {
                    context.commit('setQuantityList', res.data);

                })
                .catch((err) => {
                    console.error(err);
                })
        },
        getManage(context){
            let id = context.state.user.Coop_id;
            axios.get(`/api/member/management/${id}`)
            .then((res)=>{
                context.commit('setManage',res.data);
            })
            .catch((err)=>{
                console.error(err);
            })
        },

    }
})


export default store;
