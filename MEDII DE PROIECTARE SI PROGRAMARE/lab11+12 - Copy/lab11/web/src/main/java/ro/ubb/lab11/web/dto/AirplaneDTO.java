package ro.ubb.lab11.web.dto;

import lombok.*;

@NoArgsConstructor
@AllArgsConstructor
@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
public class AirplaneDTO extends BaseDTO<Long>{
    private String model;
    private Integer capacity;
    private String registration;
    private Integer fabricationYear;
}
