<template>
    <div class=" text-primary text-lg font-bold">
        <h3> Olá {{ usertitle }} {{ username }} {{ userlname }} como posso ajudar? </h3>
    </div>
</template>

<script>
import axios from 'axios'



export default {

    name: 'hello-user',
    data() {
        return {
            username: "",
            usertitle: "",
            userlname: "",
            
        };
    },
    methods: {
        getResponse(){
            const path = 'http://localhost:5000/'

            axios.get(path)
            .then((res) => {
                console.log(res.data)
                this.user = res.data;
                this.usertitle = res.data.usertitle;
                this.username = res.data.username;
                this.userlname = res.data.userlname;

            })
            .catch ((err) => {
                console.error(err);
            });
        }
    },
    created() {
        this.getResponse();
    },
}
</script>