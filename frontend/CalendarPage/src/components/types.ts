export interface ScheduleItem {
  time: string;
  description: string;
}

export interface DayCell {
  date: number;
  isCurrentMonth: boolean;
  hasSchedule?: boolean;
  scheduleType?: "blue" | "green" | "default";
}
