<template>
  <div class="cont">
        <headers/>
         <div class="page">
           <div class="content-block">
            <div class="titulo">
              <h1>Transações</h1>
              <hr>
            </div>
             <div class="cards">
              <div class="card-one c">
                <h1>Descarte de Sucata</h1>
                <img src="/sucata.png">
                <NuxtLink class="btn-ir" to="/sucata">Selecionar</NuxtLink>
                
              </div>

              <div class="card-two c">
                <h1>Solicitar Produtos</h1>
                <img src="/produto.png">
                <NuxtLink class="btn-ir" to="/solicitacao_produto">Selecionar</NuxtLink>
                
              </div>
              
              <div class="card-three c">
                <h1>Consultar Produtos</h1>
                <img src="/lupa.png">
                <NuxtLink class="btn-ir" to="/consulta_produto">Selecionar</NuxtLink>
              </div>

              <div class="card-four c">
                <h1>Catalogo</h1>
                <img src="/lupa.png">
                <NuxtLink class="btn-ir" to="/cod_sucata">Selecionar</NuxtLink>
              </div>
            </div> 

          </div>
        </div> 
          <footers/>
  </div>
</template>

<script>
export default {
  name: "trancoes",
  // middleware: 'auth',
}
  
</script>

<style lang="scss" scoped>
  @import '@/pages/transacoes/transacoes.scss'
</style>