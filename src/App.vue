<template>
  <div>
    <el-steps :active="currentStep" simple>
      <el-step title="选择素材"></el-step>
      <el-step title="调整位置"></el-step>
      <el-step title="打印结果"></el-step>
    </el-steps>
    <div v-if="currentStep==0">
      <div class="guide"> 输入淘宝id获得个性化的推荐和搭配 </div>
      <div style="text-align: center;">
        <el-input style="width: 200px; margin-right: 10px;" v-model="taobaoId" placeholder="输入淘宝id"></el-input>
        <el-button type="primary" v-on:click="taobaoIdCollocate"> 获取搭配 </el-button>
      </div>
      <div class="guide"> 或者，从下列商品中选择一个进行搭配</div>
      <item-selector style="margin: 0 50px 0 50px;" v-on:collocation="onCollocationReceived"></item-selector>
    </div>
    <div v-else-if="currentStep==1">
      <div class="guide"> 为搭配好的内容选择合适的位置 </div>
      <el-card style="width: fit-content; margin: auto;">
        <item-placer v-bind:collocation="collocation" style="width: 512px; height: 512px; position: relative;" ></item-placer>
      </el-card>
      <div class="rightbottom">
        <el-button v-on:click="reload">上一步</el-button>
        <el-button type="primary" v-on:click="currentStep=2">下一步</el-button>
      </div>
    </div>
    <div v-else>
      <div class="guide"> 满意的话，就打印结果吧！ </div>
      <div class="rightbottom">
        <el-button v-on:click="reload">重置</el-button>
        <el-button v-on:click="currentStep=1">上一步</el-button>
        <el-button type="primary">打印</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import ItemSelector from './components/ItemSelector'
import ItemPlacer from './components/ItemPlacer'

export default {
  name: 'app',
  components: {
    ItemSelector,
    ItemPlacer
  },
  data() {
    return {
      currentStep: 0,
      taobaoId: '',
      collocation: []
    }
  },
  methods: {
    taobaoIdCollocate: function() {
      this.$http.get('http://localhost:5000/collocation?taobaoId=' + this.taobaoId).then((response) => {
        this.onCollocationReceived(response.data)
      })
    },
    onCollocationReceived: function(data) {
      console.log(data)
      this.collocation = data
      this.currentStep = 1
    },
    reload: function() {
      this.currentStep = 0
      this.collocation = []
      this.taobaoId = ''
    }
  }
}
</script>

<style>
.guide {
  font-size: 18px;
  text-align: center;
  margin: 50px 0 50px 0;
}
.rightbottom {
  position: absolute;
  bottom: 10px;
  right: 10px;
}
</style>
