<template>
  <div>
    <el-steps :active="currentStep" simple>
      <el-step title="选择素材"></el-step>
      <el-step title="调整位置"></el-step>
      <el-step title="打印结果"></el-step>
    </el-steps>
    <div v-loading="loading" element-loading-text="滴搭正在为您服务..." element-loading-background="rgba(255, 255, 255, 0.9)">
      <div v-if="currentStep==0">
        <div class="guide"> 请输入淘宝昵称 </div>
        <div style="text-align: center;">
          <el-input style="width: 200px; margin-right: 10px;" v-model="taobaoId" placeholder="输入淘宝昵称"></el-input>
          <el-button type="primary" v-on:click="taobaoIdCollocate"> 获取搭配 </el-button>
        </div>
        <div class="guide"> 或者，从下列商品中选择一个进行搭配</div>
        <item-selector style="margin: 0 50px 0 50px;" :type-meta="typeMeta" :position-id="positionId" v-on:item-selected="itemCollocate"></item-selector>
      </div>
      <div v-else-if="currentStep==1">
        <div class="guide"> 为搭配好的内容选择合适的位置 </div>
        <el-card style="width: fit-content; margin: auto;">
          <item-placer v-bind:collocation="collocation" v-on:change="onPositionChange" style="width: 600px; height: 600px; position: relative;" ></item-placer>
        </el-card>
        <div class="rightbottom">
          <el-button v-on:click="reload">上一步</el-button>
          <el-button type="primary" v-on:click="submitPosition">下一步</el-button>
        </div>
      </div>
      <div v-else>
        <div class="guide"> 满意的话，就打印结果吧！ </div>
        <el-card style="width: fit-content; margin: auto;">
          <img id="finalImage" :src="finalImage" style="width: 600px; height: 600px; position: relative;"/>
        </el-card>
        <div class="rightbottom">
          <el-button v-on:click="reload">重置</el-button>
          <el-button v-on:click="currentStep=1">上一步</el-button>
          <el-button v-on:click="print" type="primary">打印</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ItemSelector from './components/ItemSelector'
import ItemPlacer from './components/ItemPlacer'
import http from './plugins/axios.js'

export default {
  name: 'app',
  components: {
    ItemSelector,
    ItemPlacer
  },
  data() {
    var positionId = 189856
    for(var pair of window.location.search.substr(1).split('&'))
      if (pair.split('=')[0] == 'positionId')
        positionId = pair.split('=')[1]
    return {
      positionId: positionId,
      currentStep: 0,
      loading: false,
      typeMeta: {},
      taobaoId: '',
      collocation: [],
      finalImage: ''
    }
  },
  methods: {
    taobaoIdCollocate: function() {
      this.collocate('merge.do?positionId=' + this.positionId + '&usernick=' + this.taobaoId)
    },
    itemCollocate: function(id) {
      this.collocate('merge.do?positionId=' + this.positionId + '&triggers=' + id)
    },
    collocate: function(url) {
      this.loading = true
      http.get(url, (response) => {
        this.loading = false
        if (response.success) {
          this.collocation = eval('(' + response.data.rawdata.replace(new RegExp(/(&quot;)/g), '"') + ')')
          this.currentStep = 1
        } else
          this.$message.error(response.errorMsg)
      })
    },
    onPositionChange: function(index, rect) {
      this.collocation.layers[index].x = rect.left * 2
      this.collocation.layers[index].y = rect.top * 2
      this.collocation.layers[index].width = rect.width * 2
      this.collocation.layers[index].height = rect.height * 2
    },
    submitPosition: function() {
      this.loading = true
      /* eslint-disable-next-line no-console */
      console.log(JSON.stringify(this.collocation).replace('"', '&quot;'))
      http.post('mergebyrawdata.do', JSON.stringify(this.collocation), (response) => {
        this.loading = false
        if (response.success) {
          this.finalImage = response.data
          this.currentStep = 2
        } else
          this.$message.error(response.errorMsg)
      })
    },
    reload: function() {
      this.currentStep = 0
      this.collocation = []
      this.taobaoId = ''
      this.finalImage = ''
    },
    print: function() {
      // window.print()
      var popup = window.open()
      popup.document.write('<img src="' + this.finalImage + '" style="width: 100%;"/>')
      popup.focus()
      popup.print()
    }
  },
  mounted() {
    http.get('allfrontcate.do?positionId=' + this.positionId, (response) => {
      if (response.success)
        this.typeMeta = response.data
      else
       this.$message.error(response.errorMsg)
    })
  }
}
</script>

<style>
.guide {
  font-size: 18px;
  text-align: center;
  margin: 30px 0 30px 0;
}
.rightbottom {
  position: absolute;
  bottom: 10px;
  right: 10px;
}
</style>
