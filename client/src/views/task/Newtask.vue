<template>
      <b-row>
      <b-col md="12">
        <b-card>
          <div slot="header">
            <strong>新增</strong> 任务
          </div>
          <el-form ref="form" :model="form" label-width="200px">
            <el-form-item
              label="请输入待爬取的URL"
              label-for="URL"
              :label-cols="3"
              :horizontal="true">
              <el-input id="URL" type="text" placeholder="请输入待爬取的URL"></el-input>
            </el-form-item>
            <el-form-item
              label="请选择时间"
              label-for="basicInlineCheckboxes"
              :label-cols="3"
              :horizontal="true">
                <el-time-picker
                  v-model="value2"
                  :picker-options="{
                    selectableRange: '00:00:00 - 23:59:59'
                  }"
                  placeholder="任意时间点">
                </el-time-picker>
            </el-form-item>
            <el-form-item
              label="请选择需要爬取的天数"
              label-for="dayCheckboxes"
              :label-cols="3"
              :horizontal="true">
              <b-form-checkbox-group id="dayCheckboxes" name="dayCheckboxes" :plain="true" :checked="[1]">
                <b-form-checkbox :plain="true" value="7">Sun</b-form-checkbox>
                <b-form-checkbox :plain="true" value="1">Mon</b-form-checkbox>
                <b-form-checkbox :plain="true" value="2">Tue</b-form-checkbox>
                <b-form-checkbox :plain="true" value="3">Wed</b-form-checkbox>
                <b-form-checkbox :plain="true" value="4">Thus</b-form-checkbox>
                <b-form-checkbox :plain="true" value="5">Fri</b-form-checkbox>
                <b-form-checkbox :plain="true" value="6">Sat</b-form-checkbox>
              </b-form-checkbox-group>
            </el-form-item>

            <el-form-item
              label="请选择任务开始时间"
              label-for="task_start_time"
              :label-cols="3"
              :horizontal="true">
                  <el-date-picker
                    v-model="value1"
                    type="date"
                    placeholder="任务开始日期">
                  </el-date-picker>
            </el-form-item>
            <el-form-item
              label="请选择任务结束时间"
              label-for="task_end_time"
              :label-cols="3"
              :horizontal="true">
                  <el-date-picker
                  v-model="value1"
                  type="date"
                  placeholder="任务结束日期">
                </el-date-picker>
            </el-form-item>
            
            <el-form-item
              label="任务名称"
              label-for="basicTextarea"
              :label-cols="3"
              :horizontal="true">
              <el-input id="basicTextarea" :textarea="true" :rows="9" placeholder="请输入该任务的标签"></el-input>
            </el-form-item>
            <el-form-item
              label="上传spider"
              label-for="spiderInput"
              :label-cols="3"
              :horizontal="true">
                <b-form-file id="spiderInput" :plain="true"></b-form-file>
            </el-form-item>
            <el-form-item
              label="上传item"
              label-for="itemInput"
              :label-cols="3"
              :horizontal="true">
                <b-form-file id="itemInput" :plain="true"></b-form-file>
            </el-form-item>
            <el-form-item
              label="编辑settings"
              label-for="settingsInput"
              :label-cols="3"
              :horizontal="true">
                <el-button id="settingsInput" size="sm" type="primary">打开编辑settings</el-button>
            </el-form-item>
            <el-form-item
              label="编辑middleware"
              label-for="settingsInput"
              :label-cols="3"
              :horizontal="true">
                <el-button id="settingsInput" size="sm" type="primary">打开编辑middleware</el-button>
            </el-form-item>
            <el-form-item label="请选择数据库" 
            laber-for="hosts"
            :label-cols="3"
            prop="clients">
              <el-select id='hosts' v-model="form.dbs" :placeholder="请选择数据库"
                         size="small">
                <el-option
                  v-for="item in dbOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="请选择主机" 
            laber-for="hosts"
            :label-cols="3"
            prop="clients">
              <el-select id='hosts' v-model="form.clients" multiple :placeholder="请选择主机"
                         size="small">
                <el-option
                  v-for="item in clientOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-form>
          <div slot="footer">
            <el-button size="sm" type="primary"><i class="fa fa-dot-circle-o"></i> 提交任务申请</el-button>
            <el-button size="sm" type="danger"><i class="fa fa-ban"></i> 重置</el-button>
          </div>
        </b-card>
      </b-col>
    </b-row>
</template>

<script>
  export default {
    data () {
      return {
        clientOptions: [],
        dbOptions: [],
        form: {},
        value2: new Date(2016, 9, 10, 18, 40),
        value3: new Date(2016, 9, 10, 18, 40)
      }
    }
  }
</script>
