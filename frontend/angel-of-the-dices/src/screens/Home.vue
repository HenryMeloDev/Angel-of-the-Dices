<script setup>

import Hello from "../components/helloUser.vue"

</script>


<template>
    <div class=" w-4/6 h-fit flex flex-col text-center bg-bgPrimary my-20 rounded-lg p-4">
        <div class=" w-full flex justify-center">
            <img class="" src="../assets/hero3.png" alt="angel-of-the-dices">
        </div>  
        <p class=" w-3/6 text-lg font-medium text-primary mx-auto -mt-16">
            Bem vindo ao Angel of the Dices, uma plataforma de gerenciamento de fichas de rpg e ferramentas para melhorar a experiencia de jogo online.
        </p>
        <div class=" flex justify-center gap-6 my-5">
            <a href="http://localhost:5173/sheets/" class=" w-52 border-2 border-bgSecondary bg-secondary rounded-sm">Minhas Fichas</a>
            <a href="" class=" w-52 border-2 border-secondary bg-bgSecondary rounded-sm">Criar nova ficha</a>
        </div>
        <Hello />
    </div>
</template>


<style>

</style>