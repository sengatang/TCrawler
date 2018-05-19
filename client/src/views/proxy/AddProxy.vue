<template>
    <b-row>
        <b-col md="12">
        <b-card>
          <div slot="header">
            <strong>增加代理</strong>
          </div>
          <b-form-group
            label="IP地址"
            label-for="horizEmail"
            description="请输入您需要增加的IP地址，多个IP使用逗号隔开"
            :label-cols="3"
            :horizontal="true">
            <b-form-input id="horizEmail" type="text" placeholder="输入IP..."></b-form-input>
          </b-form-group>
          <div slot="footer">
            <b-button type="submit" size="sm" variant="primary"><i class="fa fa-dot-circle-o"></i> Submit</b-button>
            <b-button type="reset" size="sm" variant="danger"><i class="fa fa-ban"></i> Reset</b-button>
          </div>
        </b-card>
      </b-col>
    </b-row>
</template>
