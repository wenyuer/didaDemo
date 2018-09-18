<template>
  <div>
    <el-row id="item-row">
      <el-col class="item-col" :span="4" :key="item.itemId" v-for="item in items">
        <el-card>
          <div class="image-wrapper">
            <img v-bind:src="item.picUrl"/>
          </div>
          <el-button type="text" v-on:click="selectItem(item.itemId)"> 继续搭配 </el-button>
        </el-card>
      </el-col>
    </el-row>
    <div>
      <el-select v-model="type">
        <el-option v-for="(v, k) in typeMeta" :key="v" :value="k" :label="v"></el-option>
      </el-select>
      <el-button id="refresh" type="primary" icon="el-icon-refresh" v-on:click="reload()"> 换一批 </el-button>
    </div>
  </div>
</template>

<script>
import http from '../plugins/axios.js'

export default {
  props: ['typeMeta', 'positionId'],
  data() {
    return {
      items: [],
      type: "0"
    }
  },
  methods: {
    reload: function() {
      http.get('loadsource.do?activityId=34455&pageSize=6&frontCateId=' + this.type + '&positionId=' + this.positionId, (response) => {
        if (response.success)
          this.items = response.data
      })
    },
    selectItem: function(id) {
      this.$emit('item-selected', id)
    }
  },
  mounted: function() {
    this.reload()
  }
}
</script>

<style scoped>
#item-row {
  margin-bottom: 10px;
}
.el-col:nth-child(n+2) .el-card {
  margin-left: 10px;
}
.el-card .image-wrapper {
  height: 150px;
  line-height: 150px;
}
.el-card img {
  margin: auto;
  display: block;
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 150px;
}
#refresh {
  margin-left: 10px;
}
</style>
