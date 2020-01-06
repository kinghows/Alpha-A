import { NgModule } from '@angular/core';
import { IonicPageModule } from 'ionic-angular';
import { realPage } from './real';

@NgModule({
  declarations: [
    realPage,
  ],
  imports: [
    IonicPageModule.forChild(realPage),
  ],
})
export class realPageModule {}
