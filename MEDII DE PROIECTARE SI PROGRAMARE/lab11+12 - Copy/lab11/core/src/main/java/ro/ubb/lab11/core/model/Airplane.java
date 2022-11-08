package ro.ubb.lab11.core.model;
import lombok.*;

import javax.persistence.Entity;
import javax.persistence.Table;

@Entity
@Table(name = "Airplanes")
@NoArgsConstructor
@AllArgsConstructor
@Data
@EqualsAndHashCode(callSuper = true)
@ToString(callSuper = true)
public class Airplane extends BaseEntity<Long>{
    private String model;
    private int capacity;
    private String registration;
    private int fabricationYear;

}
