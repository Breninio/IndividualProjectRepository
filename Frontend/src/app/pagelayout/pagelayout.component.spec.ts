import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PagelayoutComponent } from './pagelayout.component';

describe('PagelayoutComponent', () => {
  let component: PagelayoutComponent;
  let fixture: ComponentFixture<PagelayoutComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PagelayoutComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PagelayoutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
