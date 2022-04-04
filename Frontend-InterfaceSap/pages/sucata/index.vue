// Sucata
<template>
  <div class="cont">
    <headers/>
    <div class="principal">
      <form class="base" > 
        <h1>Descarte Sucata</h1>
        <input
          type="text"
          name="txtBreve"
          class="inputs"
          id="txtBreve"
          ref="den"
          placeholder="Nome da Sucata"
          v-model="sucata.txtBreve"
          required
        />
        <input
          type="text"
          name="idCenTrabFK"
          class="inputs"
          id="idCenTrabFK"
          ref="code"
          placeholder="Codigo"
          v-model="sucata.idCenTrabFK"
          required
        />
        <input
          type="text"
          name="trab"
          class="inputs"
          id="trab"
          ref="quant"
          placeholder="Quantidade (Kg)"
          v-model="sucata.trab"
          required
        />
        <input
          type="text"
          name="desc"
          class="inputs"
          id="desc"
          ref="desc"
          placeholder="Descricao"
          v-model="sucata.desc"
          required
        />
        <button type="submit" @click="fetchSucata">Enviar</button>
      </form> 
    </div>
   <footers/>
  </div>
</template>

<script>
import headers from '../../components/headers.vue'
export default {
  components: { headers },
  name: 'home',
  // middleware: 'auth',

  data() {
    return {
      sucata: {
        desc: '',
        idCenTrabFK: '',
        trab: '',
        txtBreve: '',
        idtipoOrdemFK: 1,
        idPrioridadeFK: 1,
        idLocalFK: 1,
        idtipoavtFK: 1,
        iddivisaoFK: 1,
        idCentroCustoFK: 2,
      },
    }
  },
  methods: {
    fetchSucata: async function (event) {
      event.preventDefault();
      // console.log('teste')
      // console.log(this.sucata)
      let obj = this.sucata
      let send = true
      console.log(1)
      // if ( obj.desc == '' ) { this.$refs.desc.style.borderColor='red'; }
      for (const [key, value] of Object.entries(this.sucata)) {
        if (document.getElementById(key)) {
          if (value == '') {
            send = false
            document.getElementById(key).style.borderColor = 'red'
          } else {
            document.getElementById(key).style.borderColor = '#E5E5E5'
          }
        }
      }

      if(send){
        await this.$axios
          .$post(
            'http://127.0.0.1:8000/TransacaoSucata/',
            JSON.stringify([this.sucata]),
            {
              headers: {
                'Content-Type': 'application/json',
              },
            }
          )
          .then((response) => {
            console.log(response)
            //window.onload = timedRefresh(1000);
          })
          .catch((error) => {
            console.log(error)
          })
      }
      
    },
  },
  // watch: {
  //   desc: {
  //     handler(new){
  //       let obj = this.sucata;
  //       if ( obj.desc == '' ) { this.$refs.desc.style.borderColor='red'; }
  //       else {  }
  //     }
  //   }
  // }
}
</script>

<style lang="scss" scoped>
@import '@/pages/sucata/sucata.scss';
</style>