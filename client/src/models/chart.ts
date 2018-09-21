export type ChartModes =
  'lines'
  | 'markers'
  | 'text'
  | 'lines+markers'
  | 'text+markers'
  | 'text+lines'
  | 'text+lines+markers'
  | 'none';

export type ChartTypes =
  'bar'
  | 'histogram'
  | 'pointcloud'
  | 'scatter'
  | 'scattergl'
  | 'scatter3d'
  | 'surface';

export class ChartModel {
  public name: string;
  public metricNames: string[];
  public mode: ChartModes;
  public type: ChartTypes;
}